import json
import logging
import os
import re
import requests
import uuid
from django.conf import settings
from django.core.cache import cache
from django.utils import timezone

from .models import StudentQuestionHint, Submission, Question
from .sandbox import language_for_id

logger = logging.getLogger(__name__)

# Default Ollama configuration (internal docker or local host)
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://elab-ollama:11434/api/chat")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5-coder:1.5b")
MAX_HINTS_PER_QUESTION = 3
HINT_CACHE_TTL = 604800  # 7 days in Redis cache
LLM_TIMEOUT = 15  # seconds for Ollama HTTP request

# Key for tracking in-flight LLM generation tasks in Redis
_INFLIGHT_LLM_KEY = "elab_llm_in_flight_{question_id}_{tier}"
_LLM_RESULT_KEY = "elab_llm_result_{question_id}_{tier}"
_LLM_RESULT_TTL = 120  # 2 minutes — LLM should complete within this window
_LLM_LOCK_TTL = 120  # 2 minutes — lock expires if generation hangs


def get_student_hints_for_question(student, question):
    """
    Returns existing unlocked hints for a student and question, along with metadata.
    """
    if not student.is_authenticated:
        return {
            "hints": [],
            "unlocked_count": 0,
            "max_hints": MAX_HINTS_PER_QUESTION,
            "can_unlock_more": False,
        }

    hints = list(
        StudentQuestionHint.objects.filter(student=student, question=question).order_by("hint_number")
    )
    count = len(hints)
    return {
        "hints": hints,
        "unlocked_count": count,
        "max_hints": MAX_HINTS_PER_QUESTION,
        "can_unlock_more": count < MAX_HINTS_PER_QUESTION,
        "next_hint_number": count + 1 if count < MAX_HINTS_PER_QUESTION else None,
    }


def unlock_hint_for_question(student, question):
    """
    Unlocks the next progressive hint (1 to 3) on-demand.
    Returns immediately with L4 deterministic theory hint (~20ms).
    Queues a background Celery task for LLM hint generation (~3-8s).
    Strictly capped at MAX_HINTS_PER_QUESTION (3 unique hints).
    Web workers never block on Ollama — all LLM calls happen in Celery tasks.
    """
    if not student or not student.is_authenticated:
        return None

    existing_hints = list(
        StudentQuestionHint.objects.filter(student=student, question=question).order_by("hint_number")
    )
    existing_count = len(existing_hints)

    if existing_count >= MAX_HINTS_PER_QUESTION:
        logger.info(f"Student {student.id} already has {existing_count} hints on Question {question.id}. Max reached.")
        return None

    next_hint_num = existing_count + 1

    # Concurrency check for this specific student
    existing = StudentQuestionHint.objects.filter(
        student=student, question=question, hint_number=next_hint_num
    ).first()
    if existing:
        return existing

    latest_sub = Submission.objects.filter(student=student, question=question).order_by("-id").first()

    # --- L1 CACHE: Redis fast-path (< 1ms) ---
    cache_key = f"elab_theory_hint_{question.id}_{next_hint_num}"
    hint_text = cache.get(cache_key)
    hint_type = "local_llm"

    # --- L2 CACHE: Shared Question Canonical Hint in DB (< 5ms) ---
    if not hint_text:
        canonical = StudentQuestionHint.objects.filter(
            question=question, hint_number=next_hint_num, hint_type="local_llm"
        ).exclude(hint_text="").first()
        if canonical:
            hint_text = canonical.hint_text
            cache.set(cache_key, hint_text, timeout=HINT_CACHE_TTL)
            logger.info(f"Theory hint L2 DB hit for Question {question.id} Tier {next_hint_num}.")

    # --- ASYNC LLM GENERATION: Queue Celery task, never block the web worker ---
    # The Celery task claims the Redis slot, calls Ollama, and caches the result.
    # Web workers never block on Ollama — they return L4 immediately.
    # Always queue a task; the task itself deduplicates via Redis lock.
    _enqueue_llm_generation(question.id, next_hint_num)

    # --- L4 FALLBACK: Instant Deterministic Theory Engine (< 0.1ms) ---
    if not hint_text:
        hint_text = _generate_diagnostic_hint_for_question(question, next_hint_num, latest_sub)
        hint_type = "diagnostic"

    try:
        hint_obj, _ = StudentQuestionHint.objects.get_or_create(
            student=student,
            question=question,
            hint_number=next_hint_num,
            defaults={
                "submission": latest_sub,
                "hint_text": hint_text,
                "hint_type": hint_type,
            },
        )
        return hint_obj
    except Exception as exc:
        logger.error(f"Failed to save StudentQuestionHint: {exc}", exc_info=True)
        return None


def _enqueue_llm_generation(question_id, tier):
    """
    Schedule a background Celery task to generate the LLM hint.
    Called from both unlock_hint_for_question and pregenerate_hints_for_question.
    The Celery task claims the Redis slot, calls Ollama, and caches the result.
    The web worker never blocks on Ollama.
    """
    from .tasks import generate_llm_hint_task
    generate_llm_hint_task.apply_async(
        args=[question_id, tier],
        countdown=1,  # Run 1 second from now
        expires=300,  # Expire if not picked up within 5 minutes
    )
    logger.info(f"Queued LLM generation for Question {question_id} Tier {tier}.")


def pregenerate_hints_for_question(question, force=False):
    """
    Pre-warms and caches all 3 theoretical hint tiers for a question.
    Queues background Celery tasks for LLM generation — web workers never block.
    Returns a dict with hint tiers (L4 fallback if LLM not yet ready).
    Each tier gets a queued Celery task that claims the slot and generates.
    """
    results = {}
    for tier in range(1, MAX_HINTS_PER_QUESTION + 1):
        cache_key = f"elab_theory_hint_{question.id}_{tier}"
        if not force:
            cached = cache.get(cache_key)
            if cached:
                results[tier] = cached
                continue

            canonical = StudentQuestionHint.objects.filter(
                question=question, hint_number=tier, hint_type="local_llm"
            ).exclude(hint_text="").first()
            if canonical:
                cache.set(cache_key, canonical.hint_text, timeout=HINT_CACHE_TTL)
                results[tier] = canonical.hint_text
                continue

        # Queue a Celery task to generate the LLM hint
        # The task claims the Redis slot, does the Ollama call, caches result
        _enqueue_llm_generation(question.id, tier)

        # Return L4 deterministic fallback immediately
        hint_text = _generate_diagnostic_hint_for_question(question, tier)
        cache.set(cache_key, hint_text, timeout=HINT_CACHE_TTL)
        results[tier] = hint_text

    return results


def generate_hint_for_submission(submission):
    """
    Backwards-compatible wrapper: delegates to unlock_hint_for_question.
    """
    if not submission or submission.status == Submission.Status.ACCEPTED:
        return None
    return unlock_hint_for_question(submission.student, submission.question)


def _call_local_llm(submission, hint_number, existing_hints):
    """Legacy wrapper for submission-based LLM calls."""
    return _call_local_llm_for_question(
        submission.question if submission else None,
        hint_number,
        existing_hints,
        submission=submission
    )


def _call_local_llm_for_question(question, hint_number, existing_hints, submission=None):
    """
    Queries local Ollama instance with question-tailored pure theory prompt constraints.
    Enforces ZERO CODE, NO SYNTAX, NO CODE BLOCKS.
    Returns cleaned, purely conceptual hint text grounded in the question's theory.
    """
    if not question:
        return None

    module_name = question.module.name if question.module else "Computer Science Problem Solving"

    # Progressive, pure theory-grounded pedagogical instructions (ZERO CODE)
    if hint_number == 1:
        level_instruction = (
            "HINT TIER 1 — THEORETICAL FOUNDATIONS & PROBLEM PRINCIPLES:\n"
            "- Explain the core Computer Science or mathematical theory that governs this problem (e.g., definitions, invariants, problem classification, or mathematical theorems).\n"
            "- Clarify the theoretical meaning of the problem requirements and what mathematical/logical properties must hold.\n"
            "- State the theoretical boundary conditions and edge-case limits (e.g. identity elements, empty sets, single elements, negative domains).\n"
            "- CRITICAL: ABSOLUTELY NO CODE, NO CODE FENCES, NO SYNTAX, NO VARIABLE ASSIGNMENTS, NO PSEUDO-CODE.\n"
            "- Format strictly as:\n"
            "🧠 Theoretical Foundations: <2-3 sentences explaining the core CS/mathematical theory of this question>\n"
            "🎯 Conceptual Boundary Principles: <1-2 sentences on theoretical boundaries and edge cases>"
        )
    elif hint_number == 2:
        level_instruction = (
            "HINT TIER 2 — ALGORITHMIC & PARADIGM THEORY:\n"
            "- Explain the high-level algorithmic paradigm suited for this problem (e.g. Divide and Conquer, Dynamic Programming optimal substructure, Two-Pointer convergence, Monotonicity, Greedy choice property).\n"
            "- Explain the conceptual logic and state transitions in abstract theoretical terms without any programming syntax.\n"
            "- State the theoretical time and space complexity ($O(...) notation) and explain why this theoretical approach is optimal.\n"
            "- CRITICAL: ABSOLUTELY NO CODE, NO CODE FENCES, NO SYNTAX, NO VARIABLE ASSIGNMENTS, NO PSEUDO-CODE.\n"
            "- Format strictly as:\n"
            "⚙️ Algorithmic Paradigm: <1-2 sentences on the theoretical paradigm, structural approach, and asymptotic complexity>\n"
            "🛠️ Conceptual Logic Flow: <2-3 sentences explaining the theoretical reasoning and state progression>"
        )
    else:
        level_instruction = (
            "HINT TIER 3 — INVARIANT ANALYSIS & CONCEPTUAL VERIFICATION:\n"
            "- Explain the theoretical invariants that must remain true throughout the problem execution for the solution to be proven correct.\n"
            "- Address the theoretical failure modes or logical fallacies (e.g. inductive hypothesis failure, non-terminating reduction, state transition omission, integer range overflow in discrete domains).\n"
            "- Provide conceptual guidance on what logical premise or invariant requires verification.\n"
            "- CRITICAL: ABSOLUTELY NO CODE, NO CODE FENCES, NO SYNTAX, NO VARIABLE ASSIGNMENTS, NO PSEUDO-CODE.\n"
            "- Format strictly as:\n"
            "🔍 Invariant & Correctness Theory: <1-2 sentences on the theoretical conditions or invariants required for correctness>\n"
            "⚠️ Conceptual Pitfalls: <1-2 sentences explaining theoretical edge conditions or logical fallacies>"
        )

    system_prompt = (
        "You are an academic Professor of Theoretical Computer Science and Algorithmics.\n"
        "A student is solving a programming challenge and needs conceptual, theory-based guidance.\n\n"
        "STRICT PEDAGOGICAL POLICY (ZERO CODE TOLERANCE):\n"
        "1. STRICTLY PURE THEORY ONLY: Base all guidance entirely on the theoretical foundations, mathematical definitions, algorithms, and computational principles of this question.\n"
        "2. ABSOLUTELY NO CODE: NEVER output any code, code blocks, syntax statements, variable assignments, loops, function definitions, or programming language keywords (no C/C++/Python/Java syntax). Explain all ideas in conceptual English prose and mathematical concepts.\n"
        "3. GROUNDED IN QUESTION THEORY: Directly address the theoretical nature of this specific problem title, domain, and description.\n"
        "4. CONCISE & RIGOROUS: Keep total output under 100 words in the exact requested format.\n\n"
        f"{level_instruction}"
    )

    # Extract failure context in purely conceptual terms
    status_display = submission.get_status_display() if submission else "Student in-progress solution"
    error_snippet = (submission.error_output or "").strip()[:200] if submission else "None"

    prior_hints_text = ""
    if existing_hints:
        prior_hints_text = "Prior hints unlocked for this question:\n" + "\n".join(
            [f"Hint {h.hint_number}: {h.hint_text}" for h in existing_hints]
        ) + "\nProvide a NEW, DIFFERENT, HIGHER-TIER theory hint.\n"

    user_prompt = (
        f"Question Title: {question.title}\n"
        f"Topic / Domain: {module_name}\n"
        f"Problem Description: {question.description[:400]}\n"
        f"Input / Output Context: {question.sample_input[:80] if question.sample_input else 'N/A'} -> {question.sample_output[:80] if question.sample_output else 'N/A'}\n"
        f"Current Attempt Status: {status_display}\n"
        f"Diagnostic Context: {error_snippet}\n\n"
        f"{prior_hints_text}"
        f"Provide Hint Tier #{hint_number} focusing strictly on the theory of this question. Remember: DO NOT INCLUDE ANY CODE OR CODE BLOCKS."
    )

    num_threads = int(os.environ.get("OLLAMA_NUM_THREAD", "4"))
    num_parallel = int(os.environ.get("OLLAMA_NUM_PARALLEL", "8"))

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "options": {
            "temperature": 0.2,
            "num_ctx": 512,      # 4x smaller KV cache -> drastically lower memory & CPU attention latency
            "num_predict": 90,   # Concise academic theory
            "num_thread": num_threads,
        },
        "stream": False,
    }

    resp = requests.post(OLLAMA_URL, json=payload, timeout=LLM_TIMEOUT)
    if resp.status_code == 200:
        data = resp.json()
        raw_text = data.get("message", {}).get("content", "").strip()
        cleaned = _sanitize_hint(raw_text)
        if cleaned and len(cleaned) > 20:
            return cleaned

    return None


def _sanitize_hint(text):
    """
    Strips accidental code fences, syntax keywords, and conversational filler from LLM output.
    Guarantees pure theoretical text with zero code.
    """
    if not text:
        return ""
    # Strip markdown code blocks ```...```
    text = re.sub(r"```[\w]*\n[\s\S]*?```", "", text)
    text = re.sub(r"```[\s\S]*?```", "", text)

    # Strip conversational filler
    text = re.sub(r"^(Sure!|Here is (your )?hint:?|Hint \d:?)\s*", "", text, flags=re.IGNORECASE)

    # Filter out lines that look like raw code syntax or declarations
    code_pattern = re.compile(
        r"(\b(int|float|double|char|void|def|return|printf|scanf|cin|cout|malloc|free|class|struct|public|private)\b.*[;{()]|[;{}]$|#include|import )"
    )
    cleaned_lines = []
    for line in text.split("\n"):
        stripped = line.strip()
        if code_pattern.search(stripped):
            continue
        cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)
    # Strip backticks so identifiers don't render as code blocks
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text.strip()


def _extract_failed_test_info(judge_output):
    """Extracts first failing test case stdin and expected output."""
    if not judge_output:
        return "Hidden test case evaluation failed"
    try:
        tests = json.loads(judge_output) if isinstance(judge_output, str) else judge_output
        if isinstance(tests, list):
            for t in tests:
                if not t.get("passed"):
                    stdin = str(t.get("stdin", ""))[:60]
                    expected = str(t.get("expected", ""))[:60]
                    actual = str(t.get("actual", ""))[:60]
                    return f"Input '{stdin}' -> Expected '{expected}', Got '{actual}'"
    except Exception:
        pass
    return "Test case output mismatch"


def _detect_question_topic(question):
    """Detects problem domain / data structure topic from question context."""
    text = f"{question.title} {question.description} {question.module.name if question.module else ''}".lower()

    if any(k in text for k in ["matrix", "2d array", "grid", "rows", "columns", "transpose"]):
        return "matrix"
    if any(k in text for k in ["palindrome", "anagram", "substring", "string", "character", "vowel", "reverse string"]):
        return "string"
    if any(k in text for k in ["recursion", "recursive", "backtrack", "tower of hanoi", "permutation", "combination"]):
        return "recursion"
    if any(k in text for k in ["dynamic programming", "dp", "fibonacci", "knapsack", "subsequence", "memoization"]):
        return "dp"
    if any(k in text for k in ["binary search", "search", "sort", "bubble sort", "quick sort", "merge sort"]):
        return "sorting_searching"
    if any(k in text for k in ["linked list", "node", "next pointer", "doubly linked"]):
        return "linked_list"
    if any(k in text for k in ["pointer", "malloc", "calloc", "dynamic memory", "dereference"]):
        return "pointers"
    if any(k in text for k in ["structure", "struct", "record", "union"]):
        return "structures"
    if any(k in text for k in ["prime", "gcd", "lcm", "modulo", "factorial", "digit", "sum of digits", "binary", "hexadecimal"]):
        return "math_number"
    if any(k in text for k in ["stack", "queue", "parentheses", "fifo", "lifo"]):
        return "stack_queue"
    return "general_array_loop"


def _generate_diagnostic_hint(submission, hint_number):
    """Legacy wrapper for submission-based diagnostic generation."""
    return _generate_diagnostic_hint_for_question(
        submission.question if submission else None,
        hint_number,
        submission=submission
    )


def _generate_diagnostic_hint_for_question(question, hint_number, submission=None):
    """
    Topic-aware, question-grounded theory engine for when LLM is unavailable or offline.
    Directly references the question title and domain theory with ZERO CODE.
    """
    if not question:
        return (
            "🧠 Theoretical Foundations: Understand the fundamental problem constraints, definitions, and invariant properties.\n"
            "🎯 Conceptual Boundary Principles: Analyze edge cases including empty domains, identity elements, and single inputs."
        )

    topic = _detect_question_topic(question)
    title = question.title
    status = submission.status if submission else None
    error_output = (submission.error_output or "").lower() if submission else ""

    # 1. Compilation Errors (Grammar, Lexical Scope, and Type Theory)
    if status == Submission.Status.COMPILE_ERROR and submission:
        if "expected ';'" in error_output or "expected statement before" in error_output:
            return (
                f"🧠 Formal Grammar & Parsing Theory ({title}): Programming languages are governed by formal context-free grammars. The compiler parser requires syntactic statements to strictly adhere to language production rules with proper statement delimiters.\n"
                f"🎯 Conceptual Correction: Review the grammatical structure of your theoretical statements. Ensure each conceptual statement is terminated completely before initiating the next."
            )
        if "undeclared" in error_output or "undefined" in error_output:
            return (
                f"🧠 Lexical Scope & Identifier Binding ({title}): Identifiers must be formally bound to an active lexical scope before they can be referenced in computational expressions. Unbound references indicate an out-of-scope symbol.\n"
                f"🎯 Conceptual Correction: Verify that the theoretical entity is declared within the active block scope or parameter environment before evaluating it."
            )
        if "too few arguments" in error_output or "too many arguments" in error_output:
            return (
                f"🧠 Type Theory & Function Signatures ({title}): Function calls require exact structural conformance with the declared formal parameter signature, matching arity and domain types.\n"
                f"🎯 Conceptual Correction: Verify that the arity (number of arguments) and expected conceptual domain types match the theoretical signature."
            )
        return (
            f"🧠 Formal Grammar Parsing ({title}): The parser encountered an unparsed token violating language grammar productions.\n"
            f"🎯 Conceptual Correction: Focus exclusively on the very first syntactic production error to resolve cascading compiler diagnostics."
        )

    # 2. Time Limit Exceeded (Computational Complexity & Asymptotic Growth)
    if status == Submission.Status.TLE:
        if hint_number == 1:
            return (
                f"🧠 Computational Complexity & Asymptotic Growth ({title}): The problem constraints require an algorithm with lower asymptotic time complexity. High-order polynomial or exponential growth fails when input scales.\n"
                f"🎯 Conceptual Boundary Principles: Verify that iterative and state processes strictly advance toward termination on every state transition."
            )
        elif hint_number == 2:
            return (
                f"⚙️ Algorithmic Paradigm & Complexity Reduction ({title}): A quadratic process can often be reduced to linear or linearithmic time by utilizing spatial indexing, divide-and-conquer partitioning, or frequency tables.\n"
                f"🛠️ Conceptual Logic Flow: Eliminate redundant inner scans by precomputing intermediate properties or maintaining monotonic properties across elements."
            )
        else:
            return (
                f"🔍 Redundant Subproblems & Memoization Theory ({title}): Repeating identical subproblem evaluations creates combinatorial explosion in execution time.\n"
                f"⚠️ Conceptual Pitfalls: Recognize overlapping subproblems and apply state caching or iterative bottom-up tabulation to evaluate each unique subproblem at most once."
            )

    # 3. Runtime Errors (Memory Isolation & Arithmetic Singularities)
    if status == Submission.Status.RUNTIME_ERROR:
        if "segmentation fault" in error_output or "sigsegv" in error_output or "core dumped" in error_output:
            return (
                f"🧠 Memory Addressing & Virtual Memory Architecture ({title}): Accessing memory locations outside the allocated virtual address space violates memory isolation invariants, triggering system segmentation faults.\n"
                f"🎯 Conceptual Boundary Principles: Ensure index evaluations remain strictly within the half-open interval from zero up to the cardinal size of the collection."
            )
        if "floating point exception" in error_output or "division by zero" in error_output:
            return (
                f"🧠 Arithmetic Safety Theory ({title}): In arithmetic theory, division by zero is undefined and represents an arithmetic singularity that triggers an instantaneous hardware exception.\n"
                f"🎯 Conceptual Boundary Principles: Guarantee that the divisor operand strictly excludes zero under all possible input permutations before performing modular or division operations."
            )

    # 4. Logical Errors (Theory-Grounded by Question Topic & Title)
    topic_guides = {
        "matrix": {
            1: (
                f"🧠 Discrete Coordinate Mapping & Grid Geometry ({title}): A matrix is a two-dimensional collection of elements indexed by discrete spatial coordinates (row, column). In geometric transformations such as transposition, each coordinate (r, c) reflects across the principal identity diagonal to (c, r).\n"
                f"🎯 Conceptual Boundary Principles: Treat row and column cardinalities independently; algorithms must remain correct for rectangular grids where the number of rows differs from the number of columns."
            ),
            2: (
                f"⚙️ Linear Transformation & Vector Inner Products ({title}): Matrix multiplication is theoretically defined as the linear combination of vector dot products, where each target coordinate (r, c) is the inner product of row vector r from the first matrix and column vector c from the second matrix.\n"
                f"🛠️ Conceptual Logic Flow: Establish three coordinate dimensions: the outer row sweep, the outer column sweep, and the contracting inner dimension that reduces intermediate products into a single scalar."
            ),
            3: (
                f"🔍 Coordinate Invariants & Accumulator Identity ({title}): When calculating cell-by-cell reductions, the scalar accumulator must reset to the additive algebraic identity (zero) prior to evaluating each new coordinate pair.\n"
                f"⚠️ Conceptual Pitfalls: Verify that dimensional limits prevent coordinate overflow beyond the boundary edges of the grid, especially on ragged or asymmetric dimensions."
            ),
        },
        "string": {
            1: (
                f"🧠 Sequence Theory & Reflectional Symmetry ({title}): A string is an ordered finite sequence of discrete symbols over an alphabet. Properties like palindromes represent reflectional symmetry about a central axis, where the symbol at offset k from the origin must match the symbol at offset k from the terminus.\n"
                f"🎯 Conceptual Boundary Principles: Empty sequences and single-symbol sequences are trivially symmetric. For odd-length sequences, the central median symbol serves as an invariant symmetry anchor."
            ),
            2: (
                f"⚙️ Two-Way Convergence & Frequency Distribution Theory ({title}): Symmetrical properties can be verified in linear time through two-way convergence from opposite terminal boundaries toward the center. For anagrams, the character frequency histograms over the alphabet domain must be identical.\n"
                f"🛠️ Conceptual Logic Flow: Check boundary equivalence symmetrically, advancing inward markers while preserving the invariant that all outer symbol pairs have matched."
            ),
            3: (
                f"🔍 Sequence Delimiters & Equivalence Relations ({title}): Differences in letter case, non-printable control symbols, or whitespace alter sequence length and equivalence.\n"
                f"⚠️ Conceptual Pitfalls: Ensure that sequence evaluations distinguish between semantic content symbols and terminal delimiters, and apply canonical normalization if case-insensitivity is theoretically required."
            ),
        },
        "recursion": {
            1: (
                f"🧠 Principle of Mathematical Induction ({title}): Recursion is computational induction: it relies on proving a base case for minimal inputs and establishing an inductive step where solving problem size K enables solving size K+1.\n"
                f"🎯 Conceptual Boundary Principles: The base case serves as the fundamental axiom halting infinite regression. It must comprehensively cover all minimal domain boundaries such as zero, one, or empty states."
            ),
            2: (
                f"⚙️ Recurrence Relations & Problem Decomposition ({title}): Express the problem mathematically as a recurrence relation that expresses the global solution as a combination of strictly smaller, identical subproblems.\n"
                f"🛠️ Conceptual Logic Flow: Guarantee that every recursive branch strictly reduces the distance metric to the base condition, synthesizing sub-results during the unwind phase."
            ),
            3: (
                f"🔍 Well-Founded Relations & Call Stack Invariants ({title}): Infinite recursion occurs when the reduction step fails along a well-founded ordering, allowing cyclic or non-decreasing arguments.\n"
                f"⚠️ Conceptual Pitfalls: Verify that unexpected edge cases or negative values cannot bypass the base case condition, avoiding unbounded call-stack growth."
            ),
        },
        "dp": {
            1: (
                f"🧠 Bellman's Principle of Optimality ({title}): Dynamic Programming applies when a problem satisfies optimal substructure: an optimal global solution incorporates optimal solutions to its constituent subproblems.\n"
                f"🎯 Conceptual Boundary Principles: Identify the overlapping subproblem space and establish the initial boundary states representing the base values of the recurrence."
            ),
            2: (
                f"⚙️ State Space Representation & Transition Theory ({title}): Formalize each subproblem as a discrete state that encapsulates all historical choices needed to evaluate future decisions.\n"
                f"🛠️ Conceptual Logic Flow: Establish the recurrence transition that computes larger states from prerequisite smaller states, following a topological evaluation order without redundant computation."
            ),
            3: (
                f"🔍 State Dependency Graph & Numerical Invariants ({title}): Incorrect results in dynamic programming occur when state transitions are computed before their prerequisite subproblems are fully finalized.\n"
                f"⚠️ Conceptual Pitfalls: Confirm that the order of subproblem evaluation strictly respects the topological dependency graph, and check for numerical overflow in additive state progressions."
            ),
        },
        "sorting_searching": {
            1: (
                f"🧠 Monotonicity & Binary Partitioning Theory ({title}): Searching an ordered domain relies on monotonicity: a monotonic sequence guarantees that a comparison at the midpoint divides the search domain into two partitions, discarding half the search space.\n"
                f"🎯 Conceptual Boundary Principles: If the sequence is monotonically non-decreasing, elements strictly less than the target cannot reside in the upper partition, halving the domain in logarithmic time."
            ),
            2: (
                f"⚙️ Logarithmic Search Invariants & Divide-and-Conquer ({title}): Maintain the invariant that if the target exists in the sequence, it is strictly enclosed between the active lower and upper interval boundaries.\n"
                f"🛠️ Conceptual Logic Flow: Continually contract the candidate interval toward the target or collapse to an empty domain, proving non-existence in logarithmic O(log N) steps."
            ),
            3: (
                f"🔍 Interval Degeneracy & Convergence Criteria ({title}): Off-by-one errors in binary search occur when interval updates fail to strictly shrink the domain during single-element or two-element intervals.\n"
                f"⚠️ Conceptual Pitfalls: Ensure that boundary adjustments strictly contract the interval at every comparison step to prevent infinite stagnation."
            ),
        },
        "pointers": {
            1: (
                f"🧠 Indirection & Spatial Address Theory ({title}): Pointers represent memory address indirection, decoupling the identifier of a data entity from its physical storage location in memory space.\n"
                f"🎯 Conceptual Boundary Principles: An address reference must be explicitly bound to valid, active storage before dereferencing its contents."
            ),
            2: (
                f"⚙️ Dynamic Memory Lifecycle & Ownership Semantics ({title}): Dynamic allocation creates memory blocks whose lifetime is managed independently of call frame execution scope.\n"
                f"🛠️ Conceptual Logic Flow: Track address ownership rigorously: allocate storage, verify allocation success, process data through indexed offsets, and release memory upon completion."
            ),
            3: (
                f"🔍 Null Reference & Dangling Pointer Invariants ({title}): Memory safety requires the invariant that an address is non-null and currently points to allocated storage before dereferencing.\n"
                f"⚠️ Conceptual Pitfalls: Avoid altering the base reference address during traversal, which prevents memory leaks and ensures safe reclamation."
            ),
        },
        "linked_list": {
            1: (
                f"🧠 Pointer Chaining & Node Graph Theory ({title}): A linked list is a linear sequence of discrete heap-allocated nodes, where each node stores a value and an explicit pointer reference to its successor node.\n"
                f"🎯 Conceptual Boundary Principles: Empty lists (null head) and single-element lists represent foundational boundary conditions that prevent null pointer exceptions."
            ),
            2: (
                f"⚙️ Reference Manipulation & Invariant Preservation ({title}): Structural modifications (such as insertions, reversals, or deletions) require re-linking node pointers while maintaining connectivity to avoid orphaning successor sublists.\n"
                f"🛠️ Conceptual Logic Flow: Maintain multi-pointer state tracking (such as previous, current, and next references) to update directed edges without losing list continuity."
            ),
            3: (
                f"🔍 Link Integrity & Null Termination Invariants ({title}): A finite linear list must terminate with a null successor pointer. Failing to preserve next-node references before reassigning links creates disconnected sub-graphs or memory leaks.\n"
                f"⚠️ Conceptual Pitfalls: Always buffer a reference to the next node before overwriting the link of the current node, and verify that operations on head nodes update the list anchor."
            ),
        },
        "math_number": {
            1: (
                f"🧠 Number Theory & Fundamental Theorem of Arithmetic ({title}): Every integer greater than one is either prime or can be uniquely factored into primes. Properties like divisibility, parity, and digit decomposition follow formal modular congruence rules.\n"
                f"🎯 Conceptual Boundary Principles: Analyze theoretical domain edge cases including zero, negative values, unit elements (one), and prime versus composite definitions."
            ),
            2: (
                f"⚙️ Divisor Symmetry & Positional Radix Decomposition ({title}): Factors of an integer exist in symmetric pairs centered around its square root, allowing exhaustive factor analysis within square root bounds. In positional number systems, radix division and modulo isolate individual digit magnitudes.\n"
                f"🛠️ Conceptual Logic Flow: Isolate digits systematically through modular residue and integer quotient reduction, or evaluate factor pairs symmetrically up to the square root threshold."
            ),
            3: (
                f"🔍 Discrete Domain Limits & Integer Precision Theory ({title}): Multiplicative operations on integers can exceed finite binary representation ranges, causing silent integer overflow.\n"
                f"⚠️ Conceptual Pitfalls: Account for negative signs in modular arithmetic and verify that accumulators can accommodate intermediate magnitude growth."
            ),
        },
        "structures": {
            1: (
                f"🧠 Composite Type Abstraction & Domain Encapsulation ({title}): Composite types group heterogeneous data attributes into a cohesive abstract entity, maintaining logical encapsulation and data integrity.\n"
                f"🎯 Conceptual Boundary Principles: Each composite instance maintains independent state across its member fields, preserving separation of concerns."
            ),
            2: (
                f"⚙️ Value Semantics versus Reference Semantics ({title}): Passing composite entities by reference allows shared state access without copying overhead, while value semantics guarantee isolation through deep copies.\n"
                f"🛠️ Conceptual Logic Flow: Use reference access for efficiency and shared state modifications, or value access when caller immutability is required."
            ),
            3: (
                f"🔍 Member Initialization & Memory Coherence ({title}): Accessing uninitialized composite attributes reads undefined memory state, contaminating subsequent calculations.\n"
                f"⚠️ Conceptual Pitfalls: Guarantee that all member attributes are explicitly initialized to consistent default states prior to evaluating domain operations."
            ),
        },
        "stack_queue": {
            1: (
                f"🧠 Abstract Data Type Disciplines (LIFO vs. FIFO) ({title}): A stack enforces Last-In-First-Out semantics suitable for reversible state tracking and nested parenthesis balancing, whereas a queue enforces First-In-First-Out ordering for fair chronological scheduling.\n"
                f"🎯 Conceptual Boundary Principles: Empty collections cannot be popped; operational invariants require confirming non-emptiness before attempting element extraction."
            ),
            2: (
                f"⚙️ Structural Invariants & Nested Hierarchies ({title}): In balanced syntax matching, the most recent unmatched opening delimiter must correspond directly to the next incoming closing delimiter.\n"
                f"🛠️ Conceptual Logic Flow: Push contextual states when entering a nested scope, and pop to verify symmetric closure, maintaining structural balance throughout."
            ),
            3: (
                f"🔍 Termination Balance & Underflow Invariants ({title}): Complete theoretical balance requires two invariant conditions: zero underflows during processing, and an empty collection upon reaching sequence termination.\n"
                f"⚠️ Conceptual Pitfalls: Ensure handling covers sequences with unmatched opening symbols left at termination, as well as sequences that begin with premature closing symbols."
            ),
        },
        "general_array_loop": {
            1: (
                f"🧠 Sequence Invariants & Iterative Proof Theory ({title}): Correctness in iterative algorithms relies on loop invariants: theoretical assertions that hold true before iteration begins, remain true across each step, and prove overall problem correctness upon termination.\n"
                f"🎯 Conceptual Boundary Principles: Clearly define the problem domain boundaries, accounting for empty sequences, single-element inputs, and exact start and end coordinates."
            ),
            2: (
                f"⚙️ State Accumulation & Invariant Maintenance ({title}): In cumulative algorithms, an accumulator holds the true aggregated value for the prefix of elements examined so far, starting from the algebraic identity element.\n"
                f"🛠️ Conceptual Logic Flow: Process elements systematically in sequential order, updating state strictly once per element without omission or duplicate processing."
            ),
            3: (
                f"🔍 Fencepost Invariants & Boundary Verification ({title}): Computational discrepancies often arise from fencepost errors: processing one element too few or one element beyond the valid domain.\n"
                f"⚠️ Conceptual Pitfalls: Verify that accumulator states initialize to the true algebraic identity and that termination criteria cover the entire valid domain exactly once."
            ),
        },
    }

    topic_dict = topic_guides.get(topic, topic_guides["general_array_loop"])
    return topic_dict.get(hint_number, topic_dict[1])
