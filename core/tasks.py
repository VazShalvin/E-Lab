from config.celery import app

from .services import evaluate_submission


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

