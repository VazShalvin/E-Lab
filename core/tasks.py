from config.celery import app

import logging

from .services import evaluate_submission

logger = logging.getLogger(__name__)


@app.task
def evaluate_submission_task(submission_id):
    sub = evaluate_submission(submission_id)
    return sub.pk if sub else submission_id


@app.task
def generate_submission_hint_task(submission_id):
    from .models import Submission
    from .hint_service import generate_hint_for_submission

    submission = Submission.objects.filter(pk=submission_id).first()
    if submission and submission.status != Submission.Status.ACCEPTED:
        hint = generate_hint_for_submission(submission)
        return hint.pk if hint else None
    return None


@app.task(bind=True, max_retries=3, default_retry_delay=5)
def generate_llm_hint_task(self, question_id, tier):
    """
    Background Celery task to generate an LLM hint and cache it.
    Uses Redis slot-claiming to avoid duplicate generation across workers.
    Retries up to 3 times with 5-second delay if Ollama is temporarily unavailable.
    """
    from django.core.cache import cache
    from .models import Question, StudentQuestionHint, Submission
    from .hint_service import (
        _call_local_llm_for_question,
        _generate_diagnostic_hint_for_question,
        _INFLIGHT_LLM_KEY,
        _LLM_KIND_KEY,
    )

    try:
        question = Question.objects.filter(pk=question_id, is_active=True).first()
        if not question:
            return None

        cache_key = f"elab_theory_hint_{question.id}_{tier}"
        lock_key = _INFLIGHT_LLM_KEY.format(question_id=question.id, tier=tier)

        # Claim the generation slot (idempotent — only one task succeeds)
        acquired = cache.add(lock_key, str(self.request.id), timeout=120)
        if not acquired:
            # Another task already claimed this slot; this task exits silently
            # The other task will cache the result for everyone
            logger.info(f"LLM hint slot already claimed for Q{question.id} T{tier}, skipping.")
            return None

        try:
            # Check if an LLM-generated result is already cached.
            # A cached value is only authoritative when it came from the LLM;
            # deterministic fallbacks must never short-circuit regeneration.
            cached = cache.get(cache_key)
            kind = cache.get(_LLM_KIND_KEY.format(question_id=question.id, tier=tier))
            if cached and kind == "llm":
                _upgrade_student_hints(question, tier, cached)
                return cached

            # Get existing hints for context (empty list for pre-generation)
            existing_hints = list(
                StudentQuestionHint.objects.filter(question=question, hint_number=tier)
            )
            latest_sub = (
                Submission.objects.filter(question=question)
                .order_by("-id")
                .first()
            )

            hint_text = _call_local_llm_for_question(
                question, tier, existing_hints, latest_sub
            )

            if hint_text:
                cache.set(cache_key, hint_text, timeout=604800)
                cache.set(_LLM_KIND_KEY.format(question_id=question.id, tier=tier), "llm", timeout=604800)
                _upgrade_student_hints(question, tier, hint_text)
                logger.info(f"Background LLM hint cached for Q{question.id} T{tier}.")
                return hint_text
            else:
                # LLM failed — try deterministic fallback and cache that
                hint_text = _generate_diagnostic_hint_for_question(question, tier)
                cache.set(cache_key, hint_text, timeout=604800)
                cache.set(_LLM_KIND_KEY.format(question_id=question.id, tier=tier), "diagnostic", timeout=604800)
                return hint_text

        finally:
            cache.delete(lock_key)

    except Exception as exc:
        logger.warning(f"LLM hint generation failed for Q{question_id} T{tier}: {exc}")
        # Retry with exponential backoff
        try:
            self.retry(exc=exc)
        except self.MaxRetriesExceededError:
            # Final fallback: generate deterministic hint and cache it
            try:
                question = Question.objects.filter(pk=question_id, is_active=True).first()
                if question:
                    hint_text = _generate_diagnostic_hint_for_question(question, tier)
                    cache_key = f"elab_theory_hint_{question.id}_{tier}"
                    cache.set(cache_key, hint_text, timeout=604800)
                    cache.set(_LLM_KIND_KEY.format(question_id=question.id, tier=tier), "diagnostic", timeout=604800)
                    logger.info(f"Deterministic fallback cached for Q{question.id} T{tier} after LLM failure.")
            except Exception:
                pass
        return None


def _upgrade_student_hints(question, tier, llm_text):
    """Replace stored deterministic fallback rows with the LLM-generated text."""
    from .models import StudentQuestionHint
    StudentQuestionHint.objects.filter(
        question=question, hint_number=tier, hint_type="diagnostic"
    ).update(hint_text=llm_text, hint_type="local_llm")
    logger.info(f"Upgraded stored hints to LLM text for Q{question.id} T{tier}.")
