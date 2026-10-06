# Standard library
from difflib import SequenceMatcher
from io import BytesIO
import random
import logging
# Third-party
import qrcode
# Django
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.mail import send_mail
from django.db.models import Count, Q
from django.template.loader import render_to_string
from django.utils import timezone
# Local imports
from .models import AssignedQuestion, Attendance, Certificate, CertificateRequest, Course, LabSession, Module, ModuleQuestionAssignment, Notification, Progress, Question, Submission, User
from .sandbox import run_code, language_for_id, inject_headers
from .certificate_generator import generate_certificate_pdf

logger = logging.getLogger(__name__)


def normalize_output(value):
    return (value or "").replace("\r\n", "\n").strip()


def similarity(a, b):
    return SequenceMatcher(None, a or "", b or "").ratio()


def record_attendance(student, module):
    if not student.is_authenticated or student.role != student.Role.STUDENT:
        return None

    session, _ = LabSession.objects.get_or_create(date=timezone.localdate(), module=module)
    session.students_present.add(student)
    attendance = (
        Attendance.objects.filter(student=student, session=session, logout_time__isnull=True)
        .order_by("-login_time")
        .first()
    )
    if attendance:
        return attendance
    return Attendance.objects.create(student=student, session=session)


def close_open_attendance(student):
    if not student.is_authenticated:
        return

    now = timezone.now()
    rows = Attendance.objects.filter(student=student, logout_time__isnull=True)
    for row in rows:
        row.logout_time = now
        row.time_spent_minutes = max(1, round((now - row.login_time).total_seconds() / 60))
        row.save(update_fields=["logout_time", "time_spent_minutes"])


def student_performance_band(student):
    judged = Submission.objects.filter(student=student).exclude(status__in=[Submission.Status.PENDING, Submission.Status.RUNNING])
    total = judged.count()
    if not total:
        return "new"

    accepted = judged.filter(status=Submission.Status.ACCEPTED).count()
    avg_score = sum(judged.values_list("score", flat=True)) / total
    accept_rate = accepted / total
    if accept_rate >= 0.7 and avg_score >= 70:
        return "strong"
    if accept_rate >= 0.4 and avg_score >= 40:
        return "steady"
    return "support"


def choose_adaptive_questions(student, module, difficulty, count=5):
    all_questions = list(module.questions.filter(is_active=True, difficulty=difficulty).order_by("csv_level", "id"))
    rng = random.SystemRandom()

    mandatory_qs = [q for q in all_questions if q.is_mandatory]
    optional_qs = [q for q in all_questions if not q.is_mandatory]

    if len(all_questions) <= count:
        rng.shuffle(all_questions)
        return all_questions

    needed_optional = max(0, count - len(mandatory_qs))

    accepted_ids = set(
        Submission.objects.filter(
            student=student,
            status=Submission.Status.ACCEPTED,
            question__module=module,
            question__difficulty=difficulty,
        ).values_list("question_id", flat=True)
    )
    unsolved = [question for question in optional_qs if question.id not in accepted_ids]
    pool = unsolved if len(unsolved) >= needed_optional else unsolved + [question for question in optional_qs if question.id in accepted_ids]

    band = student_performance_band(student)
    if band == "support":
        pool.sort(key=lambda question: (question.csv_level, rng.random()))
    elif band == "strong":
        pool.sort(key=lambda question: (-question.csv_level, rng.random()))
    else:
        rng.shuffle(pool)

    selected = mandatory_qs + pool[:needed_optional]
    selected = selected[:count]
    rng.shuffle(selected)
    return selected


def sync_assignment_completion(assignment):
    accepted_ids = set(
        Submission.objects.filter(
            student=assignment.student,
            status=Submission.Status.ACCEPTED,
            question__assigned_slots__assignment=assignment,
        ).values_list("question_id", flat=True)
    )
    # Also get accepted subquestion IDs for DBMS modules
    accepted_subquestion_ids = set()
    if "dbms" in assignment.module.category.lower():
        from .models import SubQuestion
        accepted_subquestion_ids = set(
            Submission.objects.filter(
                student=assignment.student,
                status=Submission.Status.ACCEPTED,
                subquestion__isnull=False,
                subquestion__main_question__assigned_slots__assignment=assignment,
            ).values_list("subquestion_id", flat=True)
        )
    
    now = timezone.now()
    slots = list(assignment.assigned_questions.select_related("question"))
    changed = False

    for index, slot in enumerate(slots):
        if not slot.unlocked_at:
            slot.unlocked_at = now
            changed = True
        
        # Check if this question is completed
        question_completed = False
        if "dbms" in assignment.module.category.lower():
            # For DBMS modules, check if all sub-questions are completed
            from .models import SubQuestion
            subquestions = SubQuestion.objects.filter(main_question=slot.question, is_active=True)
            if subquestions.exists():
                # All sub-questions must be completed
                completed_subquestion_ids = set(
                    Submission.objects.filter(
                        student=assignment.student,
                        status=Submission.Status.ACCEPTED,
                        subquestion__in=subquestions
                    ).values_list("subquestion_id", flat=True)
                )
                question_completed = len(completed_subquestion_ids) == len(subquestions)
            else:
                # No sub-questions, fall back to main question completion
                question_completed = slot.question_id in accepted_ids
        else:
            # Non-DBMS modules: check main question completion
            question_completed = slot.question_id in accepted_ids
            
        if question_completed and not slot.completed_at:
            slot.completed_at = now
            changed = True
        elif slot.completed_at and not question_completed:
            slot.completed_at = None
            changed = True
            
        if slot.completed_at and index + 1 < len(slots) and not slots[index + 1].unlocked_at:
            slots[index + 1].unlocked_at = now
            changed = True

    for slot in slots:
        if slot.pk and (slot.unlocked_at or slot.completed_at or changed):
            slot.save(update_fields=["unlocked_at", "completed_at"])

    if slots and all(slot.completed_at for slot in slots) and not assignment.completed_at:
        assignment.completed_at = now
        assignment.save(update_fields=["completed_at"])
    elif changed and assignment.completed_at and not all(slot.completed_at for slot in slots):
        assignment.completed_at = None
        assignment.save(update_fields=["completed_at"])
    return slots


def get_or_create_module_assignment(student, module, difficulty=Question.Difficulty.EASY, count=5):
    assignment, created = ModuleQuestionAssignment.objects.get_or_create(
        student=student,
        module=module,
        difficulty=difficulty,
    )
    if created or not assignment.assigned_questions.exists():
        AssignedQuestion.objects.filter(assignment=assignment).delete()
        for index, question in enumerate(choose_adaptive_questions(student, module, difficulty, count=count), start=1):
            AssignedQuestion.objects.create(
                assignment=assignment,
                question=question,
                order=index,
                unlocked_at=timezone.now(),
            )
    sync_assignment_completion(assignment)
    return assignment


def current_unlocked_question(assignment):
    sync_assignment_completion(assignment)
    return (
        assignment.assigned_questions.filter(unlocked_at__isnull=False, completed_at__isnull=True)
        .select_related("question")
        .order_by("order")
        .first()
    )


def evaluate_submission(submission_id):
    """
    Evaluate a submission against all hidden test cases.
    Uses a thread pool sized for production load (400 concurrent users).
    """
    submission = Submission.objects.select_related("question", "student").get(pk=submission_id)
    
    # Determine if this is for a sub-question
    if submission.subquestion:
        question = submission.subquestion
        # For sub-questions, we still need the main question for module/category access
        main_question = submission.question
    else:
        question = submission.question
        main_question = question
        
    tests = list(question.test_cases.filter(is_sample=False))
    if not tests:
        tests = list(question.test_cases.all())

    submission.status = Submission.Status.RUNNING
    submission.save(update_fields=["status"])

    passed = 0
    test_results = []
    worst_status = Submission.Status.ACCEPTED
    max_time = 0.0
    max_memory = 0

    # Resolve the language once from the submission (fallback to the question).
    language = language_for_id(submission.language_id or question.language_id)
    evaluated_code = inject_headers(submission.code, question.starter_code)

    def evaluate_single_test(test):
        result = run_code(
            language,
            source_code=evaluated_code,
            stdin=test.stdin,
            expected_output=test.expected_output,
            time_limit=question.time_limit,
            memory_limit_kb=question.memory_limit_kb,
        )
        return test, result

    try:
        if tests:
            # Run first test synchronously to detect compile errors early
            first_test, first_result = evaluate_single_test(tests[0])
            results = [(first_test, first_result)]

            # If the first test fails to compile, don't run the rest
            if first_result.get("status_id") != 6 and len(tests) > 1:
                # Use a larger thread pool for high concurrency (400 users)
                from concurrent.futures import ThreadPoolExecutor
                with ThreadPoolExecutor(max_workers=8) as executor:
                    rest_results = list(executor.map(evaluate_single_test, tests[1:]))
                    results.extend(rest_results)
        else:
            results = []

        for test, result in results:
            status_id = result.get("status_id")
            status_mapping = {
                3: Submission.Status.ACCEPTED,
                4: Submission.Status.WRONG_ANSWER,
                5: Submission.Status.TLE,
                6: Submission.Status.COMPILE_ERROR,
                11: Submission.Status.RUNTIME_ERROR,
            }
            status = status_mapping.get(status_id, Submission.Status.INTERNAL_ERROR)
            actual_output = normalize_output(result.get("stdout"))

            # Surface the real compiler/runtime message per test for the UI.
            error_message = (
                result.get("compile_output")
                or result.get("stderr")
                or ""
            )

            test_results.append({
                "stdin": test.stdin or "",
                "expected": test.expected_output or "",
                "actual": actual_output or "",
                "passed": status == Submission.Status.ACCEPTED,
                "status": status,
                "error": error_message,
            })

            max_time = max(max_time, float(result.get("time") or 0))
            max_memory = max(max_memory, int(result.get("memory") or 0))

            if status == Submission.Status.ACCEPTED:
                passed += 1
            elif worst_status == Submission.Status.ACCEPTED:
                worst_status = status

            if error_message:
                submission.error_output = error_message

            # A compile error is identical for every test case — stop early so
            # the student isn't kept waiting for the same failure N times.
            if status == Submission.Status.COMPILE_ERROR:
                worst_status = status
                break

        total = len(tests)
        if total == 0:
            # A question without test cases cannot be fairly accepted — flag it
            # instead of silently auto-accepting every submission with score 0.
            submission.status = Submission.Status.INTERNAL_ERROR
            submission.error_output = "No test cases configured for this question."
            submission.score = 0
            submission.judge_output = "[]"
            submission.save()
            return submission
        submission.score = round((passed / total) * 100)
        submission.status = Submission.Status.ACCEPTED if passed == total else worst_status
        submission.execution_time = max_time
        submission.memory_used = max_memory
        import json
        submission.judge_output = json.dumps(test_results)
    except Exception as exc:
        logger.error(f"Evaluation error for submission {submission_id}: {exc}", exc_info=True)
        submission.status = Submission.Status.INTERNAL_ERROR
        submission.error_output = str(exc)
    finally:
        submission.judged_at = timezone.now()
        submission.save()
        try:
            for assignment in ModuleQuestionAssignment.objects.filter(student=submission.student, module=submission.question.module):
                sync_assignment_completion(assignment)
            update_progress(submission.student, submission.question.module)
        except Exception as e:
            logger.error(f"Progress update error for submission {submission_id}: {e}")
    return submission


def update_progress(student, module):
    # For DBMS modules, count sub-questions instead of questions
    if "dbms" in module.category.lower():
        # Get all sub-questions for active main questions in this module
        from .models import SubQuestion
        subquestions = SubQuestion.objects.filter(
            main_question__module=module,
            main_question__is_active=True,
            is_active=True
        )
        total = min(12, subquestions.count())  # cap at 12 sub-questions
        attempted = subquestions.filter(submissions__student=student).distinct().count()
        completed = subquestions.filter(submissions__student=student, submissions__status=Submission.Status.ACCEPTED).distinct().count()
        completed = min(completed, total)
    else:
        questions = Question.objects.filter(module=module, is_active=True)
        if module.category in ["placement_training", "advanced_placement_training"]:
            total = min(7, questions.count())
        else:
            total = min(12, questions.count())
        attempted = questions.filter(submissions__student=student).distinct().count()
        completed = questions.filter(submissions__student=student, submissions__status=Submission.Status.ACCEPTED).distinct().count()
        completed = min(completed, total)
    percentage = (completed / total * 100) if total else 0
    progress, _ = Progress.objects.update_or_create(
        student=student,
        module=module,
        defaults={"attempted": attempted, "completed": completed, "percentage": percentage},
    )
    return progress


def student_progress(student):
    modules = Module.objects.filter(is_active=True)
    if not getattr(student, "is_faculty_like", False) and student.role != "hod":
        current_semester = getattr(student, "semester", 1) or 1
        modules = modules.filter(
            Q(course__available_from_semester__lte=current_semester) | Q(course__isnull=True)
        )
    modules = modules.annotate(total=Count("questions", filter=Q(questions__is_active=True)))
    rows = []
    for module in modules:
        rows.append(update_progress(student, module))
    return rows


def _student_primary_category(student):
    if hasattr(student, "semester"):
        sem = student.semester
        if sem in (5, 6):
            return "advanced_placement_training"
        elif sem in (3, 4):
            return "placement_training"
        elif sem == 2:
            return "python_programming"
    return "c_programming"


def overall_percentage(student, course=None):
    if course:
        target_modules = Module.objects.filter(course=course, is_active=True)
    else:
        category = _student_primary_category(student)
        target_modules = Module.objects.filter(is_active=True, category=category)
    active_modules = target_modules.count()

    total = active_modules * 12
    if total == 0:
        return 0

    assigned_qs = AssignedQuestion.objects.filter(assignment__student=student, assignment__module__in=target_modules)
    if assigned_qs.exists():
        for assignment in ModuleQuestionAssignment.objects.filter(student=student, module__in=target_modules):
            sync_assignment_completion(assignment)
        completed = assigned_qs.filter(completed_at__isnull=False).count()
    else:
        completed = (
            Submission.objects.filter(student=student, question__module__in=target_modules, question__is_active=True, status=Submission.Status.ACCEPTED)
            .values_list("question_id", flat=True)
            .distinct()
            .count()
        )

    return min(100.0, (completed / total * 100))


def certificate_eligible(student, course=None):
    if course:
        target_modules = Module.objects.filter(course=course, is_active=True)
        if target_modules.exists() and target_modules.first().category in ["placement_training", "advanced_placement_training"]:
            return False, 0
    else:
        category = _student_primary_category(student)
        target_modules = Module.objects.filter(is_active=True, category=category)
        if category in ["placement_training", "advanced_placement_training"]:
            return False, 0

    pct = overall_percentage(student, course)

    mandatory_questions = Question.objects.filter(module__in=target_modules, is_active=True, is_mandatory=True)
    mandatory_total = mandatory_questions.count()
    mandatory_done = mandatory_questions.filter(
        submissions__student=student,
        submissions__status=Submission.Status.ACCEPTED,
    ).distinct().count()
    return pct >= settings.CERTIFICATE_THRESHOLD and mandatory_done == mandatory_total, pct


def get_faculty_coordinator_for_student(student):
    """
    Determine the faculty coordinator for a student based on their completed modules/courses.
    Returns the faculty member who manages the course the student completed most questions in.
    """
    # Get modules where student has accepted submissions
    completed_modules = Module.objects.filter(
        questions__submissions__student=student,
        questions__submissions__status=Submission.Status.ACCEPTED,
        is_active=True
    ).distinct()

    if not completed_modules.exists():
        return None

    # Find the course associated with the module where student has most completions
    from django.db.models import Count
    course_completions = Course.objects.filter(
        modules__in=completed_modules
    ).annotate(
        completion_count=Count(
            'modules__questions__submissions',
            filter=Q(modules__questions__submissions__student=student,
                     modules__questions__submissions__status=Submission.Status.ACCEPTED),
            distinct=True
        )
    ).order_by('-completion_count')

    top_course = course_completions.first()
    if top_course:
        # Get faculty managing this course
        faculty = top_course.managing_faculty.first()
        if faculty:
            return faculty

    # Fallback: any faculty managing any of the student's completed modules' courses
    for course in course_completions:
        faculty = course.managing_faculty.first()
        if faculty:
            return faculty

    return None


def generate_certificate(student, course=None):
    eligible, pct = certificate_eligible(student, course)
    if not eligible:
        return None

    if not course:
        return None

    verification_hash = Certificate.make_hash(student, course, pct)
    cert, created = Certificate.objects.get_or_create(
        verification_hash=verification_hash,
        defaults={
            "student": student,
            "course": course,
            "completion_percentage": pct,
        },
    )
    if not created and cert.pdf:
        return cert

    verify_url = f"{settings.SITE_BASE_URL}/verify/{verification_hash}/"
    qr = qrcode.make(verify_url)
    qr_buffer = BytesIO()
    qr.save(qr_buffer, "PNG")
    cert.qr_code.save(f"{verification_hash}.png", ContentFile(qr_buffer.getvalue()), save=False)

    issued_at = timezone.localtime()
    issued_date = issued_at.strftime("%d %B %Y")

    from .certificate_generator import generate_certificate_pdf
    try:
        pdf_bytes = generate_certificate_pdf(
            student=student,
            percentage=pct,
            semester=course.name,
            issued_date=issued_date,
            verify_url=verify_url,
        )
        name_usn = student.usn or student.username
        cert.pdf.save(f"{name_usn}_{course.slug}.pdf", ContentFile(pdf_bytes), save=False)
    except Exception as e:
        logger.error(f"PDF generation failed for {student.username}: {e}")
    cert.save()
    notify_certificate(student, cert)
    return cert


def notify_certificate(student, certificate):
    """Send an email notification when a certificate is issued."""
    if student.email:
        send_mail(
            subject=f"{settings.SITE_NAME} - Certificate Generated",
            message=f"Congratulations! Your certificate for {certificate.course.name} is ready.",
            from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
            recipient_list=[student.email],
            fail_silently=True,
        )


def notify_faculty_of_eligible_student(student, course=None, is_reapplication=False):
    """Create a notification for all faculty members when a student applies for certificate verification."""
    eligible, pct = certificate_eligible(student, course)
    if not eligible:
        return

    faculty_users = User.objects.filter(role=User.Role.FACULTY)
    for faculty in faculty_users:
        if is_reapplication:
            title = f"Certificate Re-application: {student.display_name}"
            message = f"{student.display_name} ({student.usn or student.username}) has addressed review remarks, completed additional assignments ({pct:.1f}%), and re-applied for certificate verification."
            Notification.objects.create(
                recipient=faculty,
                notification_type=Notification.Type.CERT_ELIGIBLE,
                title=title,
                message=message,
                related_student=student,
            )
        else:
            if not Notification.objects.filter(
                recipient=faculty,
                notification_type=Notification.Type.CERT_ELIGIBLE,
                related_student=student,
            ).exists():
                Notification.objects.create(
                    recipient=faculty,
                    notification_type=Notification.Type.CERT_ELIGIBLE,
                    title=f"Certificate Approval Requested: {student.display_name}",
                    message=f"{student.display_name} ({student.usn or student.username}) has completed {pct:.1f}% of lab requirements and requested certificate verification and approval.",
                    related_student=student,
                )


def notify_hod_of_cert_request(cert_request):
    """Create a notification for all HoD users when a faculty sends a cert approval request."""
    hod_users = User.objects.filter(role=User.Role.HOD)
    past_rejections = CertificateRequest.objects.filter(student=cert_request.student, status=CertificateRequest.Status.REJECTED).exists()
    title_prefix = "Certificate Re-application Forwarded" if past_rejections else "Certificate request"
    for hod in hod_users:
        Notification.objects.create(
            recipient=hod,
            notification_type=Notification.Type.CERT_FACULTY_REQUEST,
            title=f"{title_prefix}: {cert_request.student.display_name}",
            message=f"Faculty {cert_request.requested_by_faculty.display_name} has verified and forwarded a certificate approval request for {cert_request.student.display_name} ({cert_request.completion_percentage:.1f}% complete).",
            related_student=cert_request.student,
        )


def notify_student_of_cert_decision(cert_request):
    """Notify the student and faculty when the HoD approves or rejects their certificate."""
    if cert_request.status == CertificateRequest.Status.APPROVED:
        ntype = Notification.Type.CERT_HOD_APPROVED
        title = "Certificate Approved!"
        message = "Congratulations! Your certificate has been approved by the HoD. You can now view and download your official academic diploma!"
        fac_title = f"Certificate Approved by HoD: {cert_request.student.display_name}"
        fac_msg = f"The Head of Department has approved and issued the official certificate for {cert_request.student.display_name} ({cert_request.student.usn or cert_request.student.username})."
    else:
        ntype = Notification.Type.CERT_HOD_REJECTED
        title = "Certificate Request Declined"
        message = f"Your certificate request has been declined. Notes: {cert_request.hod_notes or 'No additional notes.'}"
        fac_title = f"Certificate Declined by HoD: {cert_request.student.display_name}"
        fac_msg = f"The Head of Department declined the certificate request for {cert_request.student.display_name}. Remarks: {cert_request.hod_notes or 'No remarks provided.'}"

    Notification.objects.create(
        recipient=cert_request.student,
        notification_type=ntype,
        title=title,
        message=message,
        related_student=cert_request.student,
    )

    fac_recipients = [cert_request.requested_by_faculty] if cert_request.requested_by_faculty else User.objects.filter(role=User.Role.FACULTY)
    for fac in fac_recipients:
        if fac:
            Notification.objects.create(
                recipient=fac,
                notification_type=ntype,
                title=fac_title,
                message=fac_msg,
                related_student=cert_request.student,
            )
