import csv
import io
import json
import os
import re
import subprocess


from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.db import connection
from django.db.models import Count, Q, Sum, Value
from django.db.models.functions import Coalesce
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .forms import (
    CSVQuestionUploadForm,
    FacultyCourseSelectForm,
    ModuleForm,
    ProfileForm,
    QuestionForm,
    QuickTestCaseForm,
    StudentSignUpForm,
    SubmissionForm,
    TestCaseForm,
)
from .models import AssignedQuestion, Certificate, CertificateRequest, Course, LabSession, Module, ModuleQuestionAssignment, Notification, OpenEndedQuestion, Progress, Question, Quiz, QuizAttempt, QuizQuestion, Submission, TestCase, User
from .sandbox import run_code as sandbox_run_code, language_for_id
from .serializers import ProgressSerializer, QuestionSerializer, SubmissionSerializer
from .services import (
    certificate_eligible,
    close_open_attendance,
    current_unlocked_question,
    generate_certificate,
    get_or_create_module_assignment,
    notify_faculty_of_eligible_student,
    notify_hod_of_cert_request,
    notify_student_of_cert_decision,
    overall_percentage,
    record_attendance,
    sync_assignment_completion,
    student_progress,
    update_progress,
)
from .tasks import evaluate_submission_task


def get_faculty_modules(user):
    """Return modules managed by a faculty user via their selected courses, or all active modules if none explicitly selected."""
    if user.is_authenticated and user.is_faculty_like:
        # Fallback to managed_modules for backward compatibility during migration
        managed_courses = user.managed_courses.filter(is_active=True)
        if managed_courses.exists():
            return Module.objects.filter(course__in=managed_courses, is_active=True)
        managed_modules = user.managed_modules.filter(is_active=True)
        if managed_modules.exists():
            return managed_modules
    return Module.objects.filter(is_active=True)



class AppLoginView(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated and user.role == User.Role.HOD:
            return reverse_lazy("role_select")
        return super().get_success_url() or reverse_lazy("onboarding_overview")


class AppLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        close_open_attendance(request.user)
        if "active_role" in request.session:
            del request.session["active_role"]
        return super().dispatch(request, *args, **kwargs)


class SignUpView(CreateView):
    form_class = StudentSignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("onboarding_overview")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


def faculty_required(user):
    if not user.is_authenticated or not user.is_faculty_like:
        raise PermissionDenied


@login_required
def onboarding_overview(request):
    if request.user.role == User.Role.ADMIN:
        return redirect("admin:index")
    return render(request, "onboarding/overview.html")


@login_required
def about(request):
    if request.user.role == User.Role.ADMIN:
        return redirect("admin:index")
    return render(request, "onboarding/about.html")



@login_required
def onboarding_journey(request):
    if request.user.role == User.Role.ADMIN:
        return redirect("admin:index")
    return render(request, "onboarding/course_selection.html")


@login_required
def placement_training_overview(request):
    if request.user.role == User.Role.ADMIN:
        return redirect("admin:index")
    if not hasattr(request.user, "semester") or request.user.semester < 3:
        raise PermissionDenied
    return render(request, "placement_training/overview.html")


@login_required
def dashboard(request):
    if request.user.role == User.Role.ADMIN:
        return redirect("admin:index")

    # HoD with active role "hod" goes to HoD dashboard
    if request.user.role == User.Role.HOD:
        active_role = request.session.get("active_role")
        if active_role == "hod":
            return redirect("hod_dashboard")
        elif active_role != "faculty":
            return redirect("role_select")

    if request.user.is_faculty_like:
        courses = request.user.managed_courses.filter(is_active=True)
        if not courses.exists():
            courses = Course.objects.filter(is_active=True)
        
        course_id = request.GET.get("course")
        if course_id:
            try:
                selected_course = courses.get(id=int(course_id))
            except (ValueError, Course.DoesNotExist):
                selected_course = courses.first()
        else:
            selected_course = courses.first()

        if selected_course:
            faculty_mods = get_faculty_modules(request.user).filter(course=selected_course)
        else:
            faculty_mods = Module.objects.none()

        modules = faculty_mods.annotate(
            question_count=Count("questions"),
            active_question_count=Count("questions", filter=Q(questions__is_active=True)),
        )
        selected_category = request.GET.get("category") or "overall"
        selected_sort = request.GET.get("sort") or "rank"
        selected_department = request.GET.get("department") or ""
        if selected_sort not in {"rank", "usn"}:
            selected_sort = "rank"

        # Get all distinct departments for the filter dropdown
        departments = User.objects.exclude(
            department=""
        ).values_list("department", flat=True).distinct().order_by("department")

        progress_modules = list(modules.order_by("order", "name"))
        progress_students_qs = (
            User.objects.filter(is_staff=False, is_superuser=False)
            .exclude(role__in=[User.Role.FACULTY, User.Role.ADMIN])
        )
        if selected_department:
            progress_students_qs = progress_students_qs.filter(department=selected_department)
        selected_module = None
        if selected_category != "overall":
            try:
                selected_module_id = int(selected_category)
            except (TypeError, ValueError):
                selected_category = "overall"
            else:
                selected_module = next((module for module in progress_modules if module.id == selected_module_id), None)
                if selected_module is None:
                    selected_category = "overall"

        if selected_module:
            progress_total = min(15, selected_module.question_count)
            progress_students = progress_students_qs.annotate(
                attempted_count=Count(
                    "submissions__question",
                    filter=Q(
                        submissions__question__module=selected_module,
                    ),
                    distinct=True,
                ),
                completed_count=Count(
                    "submissions__question",
                    filter=Q(
                        submissions__question__module=selected_module,
                        submissions__status=Submission.Status.ACCEPTED,
                    ),
                    distinct=True,
                ),
            )
            selected_category_label = selected_module.name
        else:
            progress_total = sum(min(15, module.question_count) for module in progress_modules)
            progress_students = progress_students_qs.annotate(
                attempted_count=Count(
                    "submissions__question",
                    filter=Q(submissions__question__module__in=progress_modules),
                    distinct=True,
                ),
                completed_count=Count(
                    "submissions__question",
                    filter=Q(submissions__question__module__in=progress_modules, submissions__status=Submission.Status.ACCEPTED),
                    distinct=True,
                ),
            )
            selected_category_label = "Overall Progress"

        progress_tracker = []
        for student in progress_students:
            attempted = min(student.attempted_count, progress_total)
            completed = min(student.completed_count, progress_total)
            percentage = (completed / progress_total * 100) if progress_total else 0
            progress_tracker.append(
                {
                    "student": student,
                    "student_usn": student.usn or student.username,
                    "attempted": attempted,
                    "completed": completed,
                    "total": progress_total,
                    "percentage": percentage,
                }
            )

        ranked_tracker = sorted(
            progress_tracker,
            key=lambda row: (
                -row["percentage"],
                -row["completed"],
                -row["attempted"],
                row["student_usn"].lower(),
                row["student"].username.lower(),
            ),
        )
        for index, row in enumerate(ranked_tracker, start=1):
            row["rank"] = index

        if selected_sort == "usn":
            progress_tracker = sorted(
                ranked_tracker,
                key=lambda row: (row["student_usn"].lower(), row["student"].username.lower()),
            )
        else:
            progress_tracker = ranked_tracker

        recent = Submission.objects.filter(question__module__in=progress_modules).select_related("student", "question")[:12]
        recent_sessions = LabSession.objects.filter(module__in=progress_modules).select_related("module").prefetch_related("attendance_rows__student")[:6]
        students = progress_students_qs.count()
        return render(
            request,
            "faculty/dashboard.html",
            {
                "students": progress_students_qs.count(),
                "questions": Question.objects.filter(is_active=True).count(),
                "modules": modules,
                "progress_modules": progress_modules,
                "progress_tracker": progress_tracker,
                "progress_total": progress_total,
                "selected_category": selected_category,
                "selected_category_label": selected_category_label,
                "selected_sort": selected_sort,
                "courses": courses,
                "selected_course": selected_course,
                "departments": departments,
                "selected_department": selected_department,
            },
        )

    category = request.GET.get("category")
    if not category:
        if hasattr(request.user, "semester"):
            if request.user.semester >= 5:
                category = "advanced_placement_training"
            elif request.user.semester >= 3:
                category = "placement_training"
            else:
                category = "c_programming"
        else:
            category = "c_programming"
    progress_rows = student_progress(request.user)
    
    # Filter modules by semester / year for students
    if not request.user.is_faculty_like and not request.user.role == User.Role.HOD:
        # Students can only see modules for their current semester/year and below
        current_semester = getattr(request.user, "semester", 1) or 1
        current_year = (current_semester + 1) // 2
        modules = (
            Module.objects.filter(
                is_active=True,
                category=category,
            )
            .filter(
                Q(course__semester__lte=current_semester)
                | Q(course__year__lte=current_year)
                | Q(course__isnull=True)
            )
            .prefetch_related("questions")
        )
    else:
        # Faculty and HOD can see all modules
        modules = Module.objects.filter(is_active=True, category=category).prefetch_related("questions")
    progress_by_module = {row.module_id: row for row in progress_rows}
    user_submissions = Submission.objects.filter(student=request.user).values("question_id", "status")
    question_status_map = {}
    for sub in user_submissions:
        qid = sub["question_id"]
        st = sub["status"]
        if qid not in question_status_map:
            question_status_map[qid] = set()
        question_status_map[qid].add(st)

    module_cards = []
    for module in modules:
        progress = progress_by_module.get(module.id)
        module_questions = module.questions.filter(is_active=True)
        if request.user.is_faculty_like:
            module_total = module_questions.count()
            module_completed = module_questions.filter(
                submissions__student=request.user,
                submissions__status=Submission.Status.ACCEPTED,
            ).distinct().count()
            questions_for_dots = list(module_questions)
        else:
            if module.category in ["placement_training", "advanced_placement_training"]:
                module_total = min(7, module_questions.count())
            else:
                module_total = min(5, module_questions.count())
            assigned_qs = AssignedQuestion.objects.filter(
                assignment__student=request.user, assignment__module=module
            )
            if assigned_qs.exists():
                module_completed = assigned_qs.filter(completed_at__isnull=False).count()
                questions_for_dots = [aq.question for aq in assigned_qs.select_related("question")]
            else:
                module_completed = module_questions.filter(
                    submissions__student=request.user,
                    submissions__status=Submission.Status.ACCEPTED,
                ).distinct().count()
                module_completed = min(module_completed, module_total)
                questions_for_dots = list(module_questions[:module_total])

        question_statuses = []
        for q in questions_for_dots:
            st_set = question_status_map.get(q.id, set())
            if Submission.Status.ACCEPTED in st_set:
                question_statuses.append("completed")
            elif any(
                s in st_set
                for s in [
                    Submission.Status.WRONG_ANSWER,
                    Submission.Status.TLE,
                    Submission.Status.RUNTIME_ERROR,
                    Submission.Status.COMPILE_ERROR,
                    Submission.Status.INTERNAL_ERROR,
                ]
            ):
                question_statuses.append("failed")
            else:
                question_statuses.append("pending")
        if not question_statuses and module_total > 0:
            question_statuses = ["pending"] * module_total

        module_percentage = (module_completed / module_total * 100) if module_total else 0
        module_cards.append(
            {
                "module": module,
                "progress": progress,
                "percentage": module_percentage,
                "module_total": module_total,
                "module_completed": module_completed,
                "completed": module_total > 0 and module_completed == module_total,
                "question_statuses": question_statuses,
            }
        )
    pct = overall_percentage(request.user)
    dashboard_questions = Question.objects.filter(module__is_active=True, is_active=True)
    if request.user.is_faculty_like:
        questions_total = dashboard_questions.count()
        completed_total = dashboard_questions.filter(
            submissions__student=request.user,
            submissions__status=Submission.Status.ACCEPTED,
        ).distinct().count()
    else:
        questions_total = sum(card["module_total"] for card in module_cards)
        completed_total = sum(card["module_completed"] for card in module_cards)
    eligible, _ = certificate_eligible(request.user)
    certificates = request.user.certificates.all()

    # Hide certificates for 2nd years
    if hasattr(request.user, "semester") and request.user.semester >= 3:
        eligible = False
        certificates = []

    # Enhanced data for Ecosystem UI
    leaderboard_qs = (
        User.objects.filter(role=User.Role.STUDENT)
        .annotate(
            total_score=Coalesce(Sum("submissions__score"), Value(0)),
            problems_solved=Count("submissions__question", filter=Q(submissions__status=Submission.Status.ACCEPTED), distinct=True),
        )
    )

    # Efficient rank calculation
    current_user_stats = leaderboard_qs.get(id=request.user.id)
    user_rank = leaderboard_qs.filter(
        Q(total_score__gt=current_user_stats.total_score) |
        Q(total_score=current_user_stats.total_score, problems_solved__gt=current_user_stats.problems_solved) |
        Q(total_score=current_user_stats.total_score, problems_solved=current_user_stats.problems_solved, username__lt=current_user_stats.username)
    ).count() + 1

    global_leaderboard = leaderboard_qs.order_by("-total_score", "-problems_solved", "username")[:20]
    recent_activity = Submission.objects.filter(student=request.user).select_related("question")[:10]

    return render(
        request,
        "student/dashboard.html",
        {
            "category": category,
            "modules": modules,
            "module_cards": module_cards,
            "progress_rows": progress_rows,
            "overall_percentage": pct,
            "questions_total": questions_total,
            "completed_total": completed_total,
            "not_attempted_total": max(questions_total - completed_total, 0),
            "certificate_eligible": eligible,
            "certificates": certificates,
            "user_rank": user_rank,
            "global_leaderboard": global_leaderboard,
            "recent_activity": recent_activity,
        },
    )


@login_required
def module_detail(request, module_id):
    module = get_object_or_404(Module, pk=module_id, is_active=True)
    if module.category in ["placement_training", "advanced_placement_training"]:
        return redirect("module_level_detail", module_id=module.id, difficulty="medium")
        
    record_attendance(request.user, module)
    level_cards = []
    for value, label in Question.Difficulty.choices:
        questions = module.questions.filter(is_active=True, difficulty=value)
        if request.user.is_faculty_like:
            total = questions.count()
            completed = questions.filter(
                submissions__student=request.user,
                submissions__status=Submission.Status.ACCEPTED,
            ).distinct().count()
        else:
            assignment = ModuleQuestionAssignment.objects.filter(
                student=request.user, module=module, difficulty=value
            ).first()
            if assignment:
                total = assignment.assigned_questions.count()
                completed = assignment.assigned_questions.filter(completed_at__isnull=False).count()
            else:
                total = min(5, questions.count())
                completed = questions.filter(
                    submissions__student=request.user,
                    submissions__status=Submission.Status.ACCEPTED,
                ).distinct().count()
                completed = min(completed, total)

        level_cards.append(
            {
                "value": value,
                "label": label,
                "total": total,
                "completed": completed,
                "percentage": (completed / total * 100) if total else 0,
            }
        )
    return render(request, "student/module_detail.html", {"module": module, "level_cards": level_cards})


@login_required
def module_level_detail(request, module_id, difficulty):
    module = get_object_or_404(Module, pk=module_id, is_active=True)
    valid_difficulties = {value for value, _ in Question.Difficulty.choices}
    if difficulty not in valid_difficulties:
        raise PermissionDenied
    record_attendance(request.user, module)
    if request.user.is_faculty_like:
        questions = module.questions.filter(is_active=True, difficulty=difficulty)
        accepted_ids = set()
        assigned_slots = []
        current_slot = None
    else:
        assignment_count = 7 if module.category in ["placement_training", "advanced_placement_training"] else 5
        assignment = get_or_create_module_assignment(request.user, module, difficulty, count=assignment_count)
        assigned_slots = sync_assignment_completion(assignment)
        questions = [slot.question for slot in assigned_slots]
        current_slot = current_unlocked_question(assignment)
        accepted_ids = {slot.question_id for slot in assigned_slots if slot.completed_at}
    difficulty_label = dict(Question.Difficulty.choices).get(difficulty, difficulty.title())
    return render(
        request,
        "student/module_level_detail.html",
        {
            "module": module,
            "difficulty": difficulty,
            "difficulty_label": difficulty_label,
            "questions": questions,
            "assigned_slots": assigned_slots,
            "current_slot": current_slot,
            "accepted_ids": accepted_ids,
        },
    )


@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id, is_active=True)
    
    # Check semester access for students
    if hasattr(request.user, 'semester') and not request.user.is_faculty_like and not request.user.role == User.Role.HOD:
        current_semester = getattr(request.user, "semester", 1) or 1
        current_year = (current_semester + 1) // 2
        module_course = question.module.course
        if module_course:
            if module_course.semester and module_course.semester > current_semester:
                messages.error(request, "This question is not available for your semester.")
                return redirect("dashboard")
            elif module_course.year and module_course.year > current_year:
                messages.error(request, "This question is not available for your semester.")
                return redirect("dashboard")
    
    if not request.user.is_faculty_like:
        assignment = get_or_create_module_assignment(request.user, question.module, question.difficulty)
        slot = assignment.assigned_questions.filter(question=question).first()
        if not slot or not slot.unlocked_at:
            messages.error(request, "Solve your current unlocked question before opening the next one.")
            return redirect("module_level_detail", question.module_id, question.difficulty)
    record_attendance(request.user, question.module)
    latest = Submission.objects.filter(student=request.user, question=question).first()
    initial = {"code": latest.code if latest else question.starter_code}
    form = SubmissionForm(request.POST or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        if not can_submit(request.user, question):
            messages.error(request, "Please wait 30 seconds before submitting again.")
            return redirect("question_detail", question.pk)
        submission = form.save(commit=False)
        submission.student = request.user
        submission.question = question
        if question.allow_multiple_languages:
            try:
                submission.language_id = int(request.POST.get("language_id", question.language_id))
            except ValueError:
                submission.language_id = question.language_id
        else:
            submission.language_id = question.language_id
        
        session_key = f"violations_{request.user.id}_{question.id}"
        submission.proctoring_violations = request.session.get(session_key, 0)
        request.session[session_key] = 0
        
        submission.save()
        evaluate_submission_task.delay(submission.pk)
        messages.success(request, "Submission queued. We'll take you to the results shortly.")
        return redirect("submission_detail", submission.pk)

    return render(
        request,
        "student/question_detail.html",
        {
            "question": question,
            "form": form,
            "latest_submission": latest,
            "question_language": language_for_id(question.language_id),
        },
    )


@login_required
def submission_detail(request, submission_id):
    submission = get_object_or_404(Submission.objects.select_related("question"), pk=submission_id)
    if submission.student != request.user and not request.user.is_faculty_like:
        raise PermissionDenied
    return render(request, "student/submission_detail.html", {"submission": submission})


@login_required
def manual_accept_submission(request, submission_id):
    faculty_required(request.user)
    if request.method != "POST":
        raise PermissionDenied
    submission = get_object_or_404(Submission.objects.select_related("question", "student"), pk=submission_id)
    submission.status = Submission.Status.ACCEPTED
    submission.score = 100
    submission.manually_graded = True
    submission.graded_by = request.user
    submission.judged_at = timezone.now()
    submission.save(update_fields=["status", "score", "manually_graded", "graded_by", "judged_at"])
    for assignment in submission.student.module_assignments.filter(module=submission.question.module):
        sync_assignment_completion(assignment)
    update_progress(submission.student, submission.question.module)
    messages.success(request, "Submission manually marked as accepted.")
    return redirect("submission_detail", submission.pk)


@login_required
def certificate_create(request):
    if hasattr(request.user, "semester") and request.user.semester >= 3:
        raise PermissionDenied("Certificates are not available for second year students.")
        
    is_eligible, pct = certificate_eligible(request.user)
    if not is_eligible:
        messages.error(request, "You are not yet eligible for a certificate. Complete the required modules (60% threshold & mandatory questions) first.")
        return redirect("dashboard")

    cert = Certificate.objects.filter(student=request.user).first()
    approved_req = CertificateRequest.objects.filter(student=request.user, status=CertificateRequest.Status.APPROVED).first()

    if cert or approved_req:
        if not cert:
            cert = generate_certificate(request.user)
        messages.success(request, "Your official certificate is ready!")
        return redirect("certificate_detail", cert.pk)

    req = CertificateRequest.objects.filter(student=request.user).order_by("-updated_at").first()
    if req and req.status == CertificateRequest.Status.REJECTED:
        has_new_work = Submission.objects.filter(
            student=request.user,
            status=Submission.Status.ACCEPTED,
            submitted_at__gt=req.updated_at
        ).exists()
        if not has_new_work:
            messages.error(request, f"Your previous certificate request was declined (Remarks: {req.hod_notes or 'No remarks provided'}). You must complete at least one new assignment and address feedback before reapplying.")
            return redirect("dashboard")

        req = CertificateRequest.objects.create(
            student=request.user,
            status=CertificateRequest.Status.PENDING_FACULTY,
            completion_percentage=pct,
        )
        notify_faculty_of_eligible_student(request.user, is_reapplication=True)
    elif not req:
        req = CertificateRequest.objects.create(
            student=request.user,
            status=CertificateRequest.Status.PENDING_FACULTY,
            completion_percentage=pct,
        )
        notify_faculty_of_eligible_student(request.user, is_reapplication=False)

    return render(request, "certificates/under_review.html", {
        "request_obj": req,
        "percentage": pct,
    })


@login_required
def certificate_detail(request, certificate_id):
    cert = get_object_or_404(Certificate, pk=certificate_id)
    if cert.student != request.user and not request.user.is_faculty_like:
        raise PermissionDenied
    return render(request, "certificates/detail.html", {"certificate": cert})


def certificate_verify(request, verification_hash):
    cert = get_object_or_404(Certificate.objects.select_related("student"), verification_hash=verification_hash)
    return render(request, "certificates/verify.html", {"certificate": cert})


@login_required
def leaderboard(request):
    students = (
        User.objects.filter(role=User.Role.STUDENT)
        .annotate(
            total_score=Coalesce(Sum("submissions__score"), Value(0)),
            problems_solved=Count("submissions__question", filter=Q(submissions__status=Submission.Status.ACCEPTED), distinct=True),
        )
        .order_by("-total_score", "-problems_solved", "username")[:50]
    )
    return render(request, "student/leaderboard.html", {"students": students})


@login_required
def export_progress(request):
    faculty_required(request.user)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="progress.csv"'
    writer = csv.writer(response)
    writer.writerow(["USN", "Name", "Module", "Attempted", "Completed", "Percentage"])
    rows = Progress.objects.select_related("student", "module").order_by("student__usn", "module__order")
    for row in rows:
        writer.writerow(
            [
                row.student.usn,
                row.student.display_name,
                row.module.name,
                row.attempted,
                row.completed,
                f"{row.percentage:.2f}",
            ]
        )
    return response


@login_required
def attendance_report(request):
    faculty_required(request.user)
    sessions = LabSession.objects.select_related("module").prefetch_related("attendance_rows__student")[:30]
    return render(request, "faculty/attendance.html", {"sessions": sessions})


def can_submit(student, question):
    key = f"submit:{student.id}:{question.id}"
    last = cache.get(key)
    now = timezone.now()
    if last and (now - last).total_seconds() < 30:
        return False
    cache.set(key, now, 30)
    return True


def check_database():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return True
    except Exception:
        return False


def check_sandbox():
    try:
        result = subprocess.run(
            ["docker", "image", "inspect", "elab-sandbox"],
            capture_output=True,
            text=True,
            timeout=3,
        )
        return result.returncode == 0
    except Exception:
        return False


def health_check(request):
    database_ok = check_database()
    sandbox_ok = check_sandbox()
    status = 200 if database_ok and sandbox_ok else 503
    return JsonResponse(
        {
            "status": "ok" if status == 200 else "error",
            "timestamp": timezone.now().isoformat(),
            "database": "connected" if database_ok else "error",
            "sandbox": "ready" if sandbox_ok else "error",
        },
        status=status,
    )


@login_required
@require_POST
def run_code_api(request):
    import json
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, TypeError):
        return JsonResponse({"error": "Invalid JSON request body"}, status=400)

    question_id = data.get("question") or data.get("question_id")
    code = data.get("code")
    language_id = data.get("language_id")
    custom_input = data.get("custom_input")

    if not question_id or not code:
        return JsonResponse({"error": "Missing question or code parameter"}, status=400)
    
    question = get_object_or_404(Question, id=question_id, is_active=True)
    
    # Determine the execution language (use provided or fallback to question's default)
    exec_language_id = int(language_id) if language_id else question.language_id
    language = language_for_id(exec_language_id)

    # If custom input is provided, run only against that
    if custom_input is not None:
        test_cases = [
            TestCase(
                stdin=custom_input,
                expected_output="",
            )
        ]
    else:
        test_cases = question.test_cases.filter(is_sample=True).order_by("order")
        if not test_cases:
            test_cases = [
                TestCase(
                    stdin=question.sample_input,
                    expected_output=question.sample_output,
                )
            ]
    
    results = []
    for test in test_cases:
        run_result = sandbox_run_code(
            language,
            source_code=code,
            stdin=test.stdin or "",
            expected_output=test.expected_output or "",
            time_limit=question.time_limit,
            memory_limit_kb=question.memory_limit_kb,
        )
        # Custom input doesn't check against expected output for 'passed' status, 
        # it just runs. But sandbox_run_code might evaluate it anyway. 
        # If expected is empty, any output will fail if the sandbox strictly diffs it.
        # But for custom input, the frontend only cares about seeing the output.
        passed = run_result.get("status_id") == 3 if custom_input is None else True
        error_message = (
            run_result.get("compile_output")
            or run_result.get("stderr")
            or ""
        )
        results.append({
            "stdin": test.stdin or "",
            "expected": test.expected_output or "",
            "actual": run_result.get("stdout", ""),
            "passed": passed,
            "status": run_result.get("status", "Unknown"),
            "error": error_message,
        })

    return JsonResponse({
        "tests": results,
    })


@login_required
def faculty_module_form(request, module_id=None):
    faculty_required(request.user)
    module = get_object_or_404(Module, pk=module_id) if module_id else None
    form = ModuleForm(request.POST or None, instance=module)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Module saved.")
        return redirect("dashboard")
    return render(request, "faculty/form.html", {"form": form, "title": "Module", "module": module})


@login_required
def faculty_module_delete(request, module_id):
    faculty_required(request.user)
    if request.method != "POST":
        raise PermissionDenied
    module = get_object_or_404(Module, pk=module_id)
    name = module.name
    module.delete()
    messages.success(request, f"Deleted module {name}.")
    return redirect("dashboard")


@login_required
def faculty_question_bank(request, module_id=None):
    faculty_required(request.user)
    modules = Module.objects.annotate(
        question_count=Count("questions"),
        active_question_count=Count("questions", filter=Q(questions__is_active=True)),
    ).order_by("order")

    selected_module = None
    questions_by_difficulty = {}
    stats = {}

    if not module_id and modules.exists():
        module_id = modules.first().id

    if module_id:
        selected_module = get_object_or_404(Module, pk=module_id)
        all_questions = list(
            selected_module.questions
            .annotate(test_count=Count("test_cases"))
            .order_by("difficulty", "csv_level", "title")
        )
        for diff_value, diff_label in Question.Difficulty.choices:
            qs = [q for q in all_questions if q.difficulty == diff_value]
            questions_by_difficulty[diff_label] = qs

        stats = {
            "total": len(all_questions),
            "easy": len([q for q in all_questions if q.difficulty == Question.Difficulty.EASY]),
            "medium": len([q for q in all_questions if q.difficulty == Question.Difficulty.MEDIUM]),
            "hard": len([q for q in all_questions if q.difficulty == Question.Difficulty.HARD]),
            "mandatory": len([q for q in all_questions if q.is_mandatory]),
        }

    return render(
        request,
        "faculty/question_bank.html",
        {
            "modules": modules,
            "selected_module": selected_module,
            "questions_by_difficulty": questions_by_difficulty,
            "stats": stats,
        },
    )


def module_name_from_csv(filename):
    filename = os.path.basename(filename)
    stem = filename.rsplit(".", 1)[0]
    match = re.match(r"Module(\d+)_(.+)", stem, re.IGNORECASE)
    if not match:
        name = re.sub(r"[_\s]+(?:Full|Levels)$", "", stem, flags=re.IGNORECASE)
        return name.replace("_", " ").strip(), 1
    order = int(match.group(1))
    raw_name = re.sub(r"[_\s]+(?:Full|Levels)$", "", match.group(2), flags=re.IGNORECASE)
    name = raw_name.replace("_", " ").replace("IO", "I/O").strip()
    name = name.replace("Operators Expressions", "Operators & Expressions")
    name = name.replace("Conditionals Loops", "Conditionals & Loops")
    return name, order


def difficulty_from_csv(value):
    value = (value or "").strip().lower()
    if value == "medium":
        return Question.Difficulty.MEDIUM
    if value in {"hard", "expert"}:
        return Question.Difficulty.HARD
    return Question.Difficulty.EASY


def question_description_from_row(row, module):
    explicit = (row.get("Problem_Statement") or row.get("Description") or "").strip()
    if explicit:
        return explicit

    topic = row.get("Topic", "").strip()
    level = row.get("Level", "").strip()
    level_range = row.get("Level_Range", "").strip()
    difficulty = row.get("Difficulty", "").strip()
    return (
        f"Topic: {topic}\n"
        f"Module: {module.name}\n"
        f"Level: {level} ({level_range})\n"
        f"Difficulty: {difficulty}\n\n"
        "Write a C program for this exercise. Read all input from stdin and print only the exact expected output.\n\n"
        "Faculty note: replace this scaffold with the complete problem statement, input format, output format, "
        "constraints, and examples before making the question live."
    )


def starter_code_for_csv_question(row=None):
    explicit = ((row or {}).get("Starter_Code") or "").strip()
    if explicit:
        return explicit
    return (
        "#include <stdio.h>\n\n"
        "int main(void)\n"
        "{\n"
        "    /* Read from stdin. Do not print prompts unless required. */\n"
        "    return 0;\n"
        "}\n"
    )


def bool_from_csv(value, default=False):
    value = str(value or "").strip().lower()
    if value in {"1", "true", "yes", "y", "active"}:
        return True
    if value in {"0", "false", "no", "n", "inactive", "draft"}:
        return False
    return default


def row_test_cases(row):
    cases = []
    for index in range(1, 21):
        stdin = row.get(f"Test{index}_Input")
        expected = row.get(f"Test{index}_Output")
        if expected is None:
            expected = row.get(f"Test{index}_Expected_Output")
        if expected is None:
            continue
        if str(stdin or "").strip() == "" and str(expected or "").strip() == "":
            continue
        cases.append((index, stdin or "", expected or ""))
    return cases


def extract_text_from_pdf(file_obj):
    """Extract raw text from a PDF file using pypdf."""
    import pypdf
    reader = pypdf.PdfReader(file_obj)
    text_parts = []
    for page in reader.pages:
        text_parts.append(page.extract_text() or "")
    return "\n".join(text_parts)


def import_question_text(file_name, text, faculty):
    """Parse structured text (from TXT or PDF) into questions and test cases."""
    module_name, order = module_name_from_csv(file_name)
    module, _ = Module.objects.update_or_create(
        name=module_name,
        defaults={
            "description": f"Imported question bank for {module_name}.",
            "level": order,
            "order": order,
            "is_active": True,
        },
    )

    questions_raw = re.split(r'={3,}\s*QUESTION\s*={3,}', text)
    created = 0
    updated = 0
    active = 0
    test_cases_count = 0
    imported_slugs = []

    for q_index, q_block in enumerate(questions_raw, start=1):
        q_block = q_block.strip()
        if not q_block:
            continue

        # Split question body from test cases
        parts = re.split(r'={3,}\s*TEST\s*CASE\s*\d+\s*={3,}', q_block)
        q_body = parts[0].strip()
        test_blocks = parts[1:] if len(parts) > 1 else []

        # Parse question fields
        title = ""
        difficulty_str = "easy"
        level = "1"
        description = ""
        starter_code = ""

        lines = q_body.split("\n")
        current_field = None
        field_lines = []

        for line in lines:
            stripped = line.strip()
            lower = stripped.lower()
            if lower.startswith("title:"):
                if current_field == "description":
                    description = "\n".join(field_lines).strip()
                elif current_field == "starter_code":
                    starter_code = "\n".join(field_lines).strip()
                current_field = "title"
                title = stripped[len("title:"):].strip()
                field_lines = []
            elif lower.startswith("difficulty:"):
                if current_field == "description":
                    description = "\n".join(field_lines).strip()
                elif current_field == "starter_code":
                    starter_code = "\n".join(field_lines).strip()
                current_field = "difficulty"
                difficulty_str = stripped[len("difficulty:"):].strip().lower()
                field_lines = []
            elif lower.startswith("level:"):
                if current_field == "description":
                    description = "\n".join(field_lines).strip()
                elif current_field == "starter_code":
                    starter_code = "\n".join(field_lines).strip()
                current_field = "level"
                level = stripped[len("level:"):].strip()
                field_lines = []
            elif lower.startswith("description:"):
                if current_field == "starter_code":
                    starter_code = "\n".join(field_lines).strip()
                current_field = "description"
                rest = stripped[len("description:"):].strip()
                field_lines = [rest] if rest else []
            elif lower.startswith("starter code:") or lower.startswith("starter_code:"):
                if current_field == "description":
                    description = "\n".join(field_lines).strip()
                current_field = "starter_code"
                rest = stripped.split(":", 1)[1].strip()
                field_lines = [rest] if rest else []
            else:
                field_lines.append(line)

        # Flush remaining
        if current_field == "description":
            description = "\n".join(field_lines).strip()
        elif current_field == "starter_code":
            starter_code = "\n".join(field_lines).strip()

        if not title:
            title = f"Q{q_index:03d} - {module_name} (Level {level})"

        slug = slugify(f"Q{q_index:03d}-{title}")[:180]
        imported_slugs.append(slug)

        # Parse test cases
        tests = []
        for tc_index, tc_block in enumerate(test_blocks, start=1):
            tc_block = tc_block.strip()
            stdin = ""
            expected = ""
            tc_field = None
            tc_lines = []
            for tc_line in tc_block.split("\n"):
                tc_stripped = tc_line.strip()
                tc_lower = tc_stripped.lower()
                if tc_lower.startswith("input:"):
                    if tc_field == "output":
                        expected = "\n".join(tc_lines).strip()
                    tc_field = "input"
                    rest = tc_stripped[len("input:"):].strip()
                    tc_lines = [rest] if rest else []
                elif tc_lower.startswith("output:") or tc_lower.startswith("expected output:") or tc_lower.startswith("expected_output:"):
                    if tc_field == "input":
                        stdin = "\n".join(tc_lines).strip()
                    tc_field = "output"
                    rest = tc_stripped.split(":", 1)[1].strip()
                    tc_lines = [rest] if rest else []
                else:
                    tc_lines.append(tc_line)
            if tc_field == "input":
                stdin = "\n".join(tc_lines).strip()
            elif tc_field == "output":
                expected = "\n".join(tc_lines).strip()
            if stdin or expected:
                tests.append((tc_index, stdin, expected))

        difficulty = difficulty_from_csv(difficulty_str)
        has_content = bool(description.strip())
        has_tests = bool(tests)

        obj, was_created = Question.objects.update_or_create(
            module=module,
            slug=slug,
            defaults={
                "title": title,
                "description": description or f"Topic: {title}\nModule: {module_name}\nLevel: {level}\nDifficulty: {difficulty_str}\n\nWrite a C program for this exercise.",
                "difficulty": difficulty,
                "csv_level": int(level or 1),
                "starter_code": starter_code or starter_code_for_csv_question(None),
                "language_id": 50,
                "time_limit": 2.0,
                "memory_limit_kb": 128000,
                "is_active": has_content and has_tests,
                "created_by": faculty,
            },
        )
        for test_order, stdin, expected in tests:
            TestCase.objects.update_or_create(
                question=obj,
                order=test_order,
                defaults={
                    "stdin": stdin,
                    "expected_output": expected,
                    "is_sample": test_order == 1,
                },
            )
        if tests:
            TestCase.objects.filter(question=obj).exclude(order__in=[c[0] for c in tests]).delete()
        test_cases_count += len(tests)
        if obj.is_active:
            active += 1
        if was_created:
            created += 1
        else:
            updated += 1

    return {
        "module": module,
        "created": created,
        "updated": updated,
        "active": active,
        "test_cases": test_cases_count,
        "stale_deleted": 0,
        "replaced_deleted": 0,
        "assignments_reset": 0,
    }


def _module_for_import(filename, category="c_programming", module_name=None, order=None):
    """Create/update the target Module for an imported bank file and link its Course."""
    if module_name is None:
        module_name, order = module_name_from_csv(filename)
    module, _ = Module.objects.update_or_create(
        name=module_name,
        defaults={
            "description": f"Imported question bank for {module_name}.",
            "level": order,
            "order": order,
            "is_active": True,
            "category": category,
        },
    )

    # Auto-link module to its Course (create if needed)
    COURSE_META = {
        "c_programming": "C Programming",
        "python_programming": "Python Programming",
    }
    course_name = COURSE_META.get(category, category.replace("_", " ").title())
    course, _ = Course.objects.get_or_create(
        slug=category,
        defaults={"name": course_name, "is_active": True},
    )
    if module.course_id != course.pk:
        module.course = course
        module.save(update_fields=["course"])
    return module


def _canonical_question_to_row(question):
    """Project a canonical-schema question (docs/QUESTION_JSON_SCHEMA.md) onto the
    flat row shape shared by the CSV and JSON importers."""
    row = {
        "Question_ID": question["question_id"],
        "Title": question["title"],
        "Topic": question.get("topic", ""),
        "Level": question.get("level", 1),
        "Level_Range": question.get("level_range", ""),
        "Difficulty": question.get("difficulty", "easy"),
        "Problem_Statement": question.get("description", ""),
        "Starter_Code": question.get("starter_code", ""),
        "Time_Limit": question.get("time_limit", 2.0),
        "Memory_Limit_KB": question.get("memory_limit_kb", 128000),
        "Max_Score": question.get("max_score", 1),
        "Is_Active": question.get("is_active", True),
        "Is_Mandatory": question.get("is_mandatory", False),
        "Allow_Multiple_Languages": question.get("allow_multiple_languages", False),
    }
    for index, case in enumerate(question.get("test_cases", []), start=1):
        row[f"Test{index}_Input"] = case.get("input", "")
        row[f"Test{index}_Output"] = case.get("expected_output", "")
    return row


def _import_rows_into_module(data, module, faculty, file_name):
    created = 0
    updated = 0
    active = 0
    test_cases = 0
    imported_slugs = []
    replace_bank = "_levels" in file_name.lower()
    for index, row in enumerate(data, start=1):
        question_id = str(row.get("Question_ID") or f"Q{index:03d}").strip()
        topic = str(row.get("Topic") or "Question").strip()
        level = str(row.get("Level") or "1").strip()
        title = str(row.get("Title") or f"{question_id} - {topic} (Level {level})").strip()
        slug = slugify(f"{question_id}-{topic}-level-{level}")[:180]
        imported_slugs.append(slug)
        tests = row_test_cases(row)
        active_default = bool(tests) and bool((row.get("Problem_Statement") or row.get("Description") or "").strip())
        obj, was_created = Question.objects.update_or_create(
            module=module,
            slug=slug,
            defaults={
                "title": title,
                "description": question_description_from_row(row, module),
                "difficulty": difficulty_from_csv(row.get("Difficulty")),
                "csv_level": int(row.get("Level") or 1),
                "level_range": (row.get("Level_Range") or "").strip(),
                "starter_code": starter_code_for_csv_question(row),
                "language_id": 50,
                "time_limit": float(row.get("Time_Limit") or 2.0),
                "memory_limit_kb": int(row.get("Memory_Limit_KB") or 128000),
                "allow_multiple_languages": bool_from_csv(row.get("Allow_Multiple_Languages"), default=False),
                "is_mandatory": bool_from_csv(row.get("Is_Mandatory"), default=False),
                "is_active": bool_from_csv(row.get("Is_Active"), default=active_default),
                "created_by": faculty,
            },
        )
        for test_order, stdin, expected in tests:
            TestCase.objects.update_or_create(
                question=obj,
                order=test_order,
                defaults={
                    "stdin": stdin,
                    "expected_output": expected,
                    "is_sample": test_order == 1,
                },
            )
        if tests:
            TestCase.objects.filter(question=obj).exclude(order__in=[case[0] for case in tests]).delete()
        test_cases += len(tests)
        if obj.is_active:
            active += 1
        if was_created:
            created += 1
        else:
            updated += 1

    stale_deleted = 0
    if test_cases:
        stale_qs = (
            Question.objects.filter(module=module, is_active=False, description__startswith="Topic:")
            .annotate(test_count=Count("test_cases"))
            .filter(test_count=0)
            .exclude(slug__in=imported_slugs)
        )
        stale_deleted, _ = stale_qs.delete()

    replaced_deleted = 0
    assignments_reset = 0
    if replace_bank:
        replaced_deleted, _ = Question.objects.filter(module=module).exclude(slug__in=imported_slugs).delete()
        assignments_reset, _ = ModuleQuestionAssignment.objects.filter(module=module).delete()

    return {
        "module": module,
        "created": created,
        "updated": updated,
        "active": active,
        "test_cases": test_cases,
        "stale_deleted": stale_deleted,
        "replaced_deleted": replaced_deleted,
        "assignments_reset": assignments_reset,
    }


def import_question_json(file_obj, faculty, category="c_programming"):
    """Import question banks from JSON.

    Accepts both the canonical schema ({"category", "modules": [...]} — see
    docs/QUESTION_JSON_SCHEMA.md) and the legacy flat CSV-row list format.
    """
    data = json.loads(file_obj.read().decode("utf-8-sig"))

    if isinstance(data, dict) and "modules" in data:
        category = data.get("category") or category
        results = []
        for mod in data.get("modules", []):
            module = _module_for_import(
                file_obj.name,
                category=category,
                module_name=str(mod.get("module") or module_name_from_csv(file_obj.name)[0]),
                order=int(mod.get("module_order") or 1),
            )
            rows = [_canonical_question_to_row(q) for q in mod.get("questions", [])]
            results.append(_import_rows_into_module(rows, module, faculty, file_obj.name))
        return {
            "module": results[0]["module"] if results else None,
            "modules": [row["module"] for row in results],
            "created": sum(row["created"] for row in results),
            "updated": sum(row["updated"] for row in results),
            "active": sum(row["active"] for row in results),
            "test_cases": sum(row["test_cases"] for row in results),
            "stale_deleted": sum(row["stale_deleted"] for row in results),
            "replaced_deleted": sum(row["replaced_deleted"] for row in results),
            "assignments_reset": sum(row["assignments_reset"] for row in results),
        }

    # Legacy format: flat list of CSV-style row dicts.
    required = {"Question_ID", "Topic", "Level", "Difficulty"}
    if data:
        missing = required.difference(data[0].keys())
        if missing:
            raise ValueError(f"{file_obj.name}: missing keys {', '.join(sorted(missing))}")
    module = _module_for_import(file_obj.name, category=category)
    return _import_rows_into_module(data, module, faculty, file_obj.name)


def import_question_csv(file_obj, faculty, category="c_programming"):
    """Import question banks from a CSV file with the documented columns
    (Question_ID, Topic, Level, Difficulty, ..., Test1_Input, Test1_Output, ...)."""
    text = file_obj.read().decode("utf-8-sig")
    data = list(csv.DictReader(io.StringIO(text)))
    required = {"Question_ID", "Topic", "Level", "Difficulty"}
    if data:
        missing = required.difference(data[0].keys())
        if missing:
            raise ValueError(f"{file_obj.name}: missing keys {', '.join(sorted(missing))}")
    module = _module_for_import(file_obj.name, category=category)
    return _import_rows_into_module(data, module, faculty, file_obj.name)


@login_required
def download_demo_file(request, file_type):
    faculty_required(request.user)
    if file_type == "txt":
        content = """=== QUESTION ===
Title: Sum of Two Integers
Difficulty: Easy
Level: 1
Description: Write a C program to read two space-separated integers from standard input and print their sum.
Starter Code: #include <stdio.h>
int main() {
    // Write your code here
    return 0;
}
=== TEST CASE 1 ===
Input: 10 20
Output: 30
=== TEST CASE 2 ===
Input: -5 15
Output: 10

=== QUESTION ===
Title: Factorial of a Number
Difficulty: Medium
Level: 2
Description: Write a C program to calculate the factorial of a given non-negative integer N.
Starter Code: #include <stdio.h>
int main() {
    // Write your code here
    return 0;
}
=== TEST CASE 1 ===
Input: 5
Output: 120
=== TEST CASE 2 ===
Input: 0
Output: 1
"""
        response = HttpResponse(content, content_type="text/plain")
        response["Content-Disposition"] = 'attachment; filename="demo_questions_format.txt"'
        return response
    elif file_type == "csv":
        content = """Question_ID,Topic,Level,Difficulty,Level_Range,Status,Score,Max_Score,Problem_Statement,Starter_Code,Is_Active,Test1_Input,Test1_Output,Test2_Input,Test2_Output
Q001,Basics I/O,1,Easy,1-5,Active,10,10,"Write a C program to read two integers and output their sum.","#include <stdio.h>\nint main() {\n    return 0;\n}",True,"10 20","30","-5 15","10"
Q002,Loops,2,Medium,6-10,Active,15,15,"Write a C program to calculate the factorial of a given integer N.","#include <stdio.h>\nint main() {\n    return 0;\n}",True,"5","120","0","1"
"""
        response = HttpResponse(content, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="demo_questions_format.csv"'
        return response
    elif file_type == "pdf":
        html_string = """
        <html>
        <head>
            <style>
                body { font-family: 'Helvetica', 'Arial', sans-serif; color: #1e293b; line-height: 1.5; padding: 30px; }
                h1 { color: #2e3093; border-bottom: 2px solid #4f46e5; padding-bottom: 10px; margin-bottom: 20px; font-size: 24px; }
                p.intro { color: #64748b; font-size: 14px; margin-bottom: 25px; }
                .question-block { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px; margin-bottom: 25px; }
                .block-header { font-weight: bold; color: #4f46e5; font-size: 16px; margin-bottom: 10px; border-bottom: 1px solid #e2e8f0; padding-bottom: 5px; }
                .field { margin-bottom: 8px; font-size: 14px; }
                .field-label { font-weight: bold; color: #334155; }
                pre { background: #1e293b; color: #f8fafc; padding: 12px; border-radius: 6px; font-family: monospace; font-size: 13px; margin: 8px 0; white-space: pre-wrap; }
                .test-case { background: #ffffff; border-left: 4px solid #06b6d4; padding: 10px 15px; margin: 10px 0; border-radius: 0 6px 6px 0; }
            </style>
        </head>
        <body>
            <h1>CCE e-Lab: Question Import PDF Demo Format</h1>
            <p class="intro">When importing PDF or TXT question files into the e-Lab portal, structure each question using the exact block format shown below. The importer parses the <b>=== QUESTION ===</b> and <b>=== TEST CASE ===</b> delimiters.</p>
            
            <div class="question-block">
                <div class="block-header">=== QUESTION ===</div>
                <div class="field"><span class="field-label">Title:</span> Sum of Two Integers</div>
                <div class="field"><span class="field-label">Difficulty:</span> Easy</div>
                <div class="field"><span class="field-label">Level:</span> 1</div>
                <div class="field"><span class="field-label">Description:</span> Write a C program to read two space-separated integers from standard input and print their sum.</div>
                <div class="field"><span class="field-label">Starter Code:</span>
<pre>#include &lt;stdio.h&gt;
int main() {
    // Write your code here
    return 0;
}</pre>
                </div>
                
                <div class="test-case">
                    <div class="block-header" style="color: #06b6d4; font-size: 14px;">=== TEST CASE 1 ===</div>
                    <div class="field"><span class="field-label">Input:</span> 10 20</div>
                    <div class="field"><span class="field-label">Output:</span> 30</div>
                </div>

                <div class="test-case">
                    <div class="block-header" style="color: #06b6d4; font-size: 14px;">=== TEST CASE 2 ===</div>
                    <div class="field"><span class="field-label">Input:</span> -5 15</div>
                    <div class="field"><span class="field-label">Output:</span> 10</div>
                </div>
            </div>

            <div class="question-block">
                <div class="block-header">=== QUESTION ===</div>
                <div class="field"><span class="field-label">Title:</span> Factorial of a Number</div>
                <div class="field"><span class="field-label">Difficulty:</span> Medium</div>
                <div class="field"><span class="field-label">Level:</span> 2</div>
                <div class="field"><span class="field-label">Description:</span> Write a C program to calculate the factorial of a given non-negative integer N.</div>
                <div class="field"><span class="field-label">Starter Code:</span>
<pre>#include &lt;stdio.h&gt;
int main() {
    // Write your code here
    return 0;
}</pre>
                </div>
                
                <div class="test-case">
                    <div class="block-header" style="color: #06b6d4; font-size: 14px;">=== TEST CASE 1 ===</div>
                    <div class="field"><span class="field-label">Input:</span> 5</div>
                    <div class="field"><span class="field-label">Output:</span> 120</div>
                </div>

                <div class="test-case">
                    <div class="block-header" style="color: #06b6d4; font-size: 14px;">=== TEST CASE 2 ===</div>
                    <div class="field"><span class="field-label">Input:</span> 0</div>
                    <div class="field"><span class="field-label">Output:</span> 1</div>
                </div>
            </div>
        </body>
        </html>
        """
        from weasyprint import HTML
        pdf_bytes = HTML(string=html_string).write_pdf()
        response = HttpResponse(pdf_bytes, content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="demo_questions_format.pdf"'
        return response
    else:
        raise PermissionDenied("Invalid demo file type requested.")


@login_required
def faculty_question_upload(request):
    faculty_required(request.user)
    form = CSVQuestionUploadForm(request.POST or None, request.FILES or None)
    results = []
    if request.method == "POST" and form.is_valid():
        for file_obj in form.cleaned_data["files"]:
            try:
                ext = os.path.splitext(file_obj.name)[1].lower()
                if ext == ".pdf":
                    text = extract_text_from_pdf(file_obj)
                    results.append(import_question_text(file_obj.name, text, request.user))
                elif ext == ".txt":
                    text = file_obj.read().decode("utf-8-sig")
                    results.append(import_question_text(file_obj.name, text, request.user))
                elif ext == ".json":
                    results.append(import_question_json(file_obj, request.user))
                else:
                    results.append(import_question_csv(file_obj, request.user))
            except Exception as exc:
                messages.error(request, str(exc))
        if results:
            total_created = sum(row["created"] for row in results)
            total_updated = sum(row["updated"] for row in results)
            total_active = sum(row["active"] for row in results)
            total_tests = sum(row["test_cases"] for row in results)
            total_deleted = sum(row["stale_deleted"] for row in results)
            total_replaced = sum(row["replaced_deleted"] for row in results)
            total_reset = sum(row["assignments_reset"] for row in results)
            messages.success(
                request,
                f"Imported {total_created} new questions, updated {total_updated}, activated {total_active}, synced {total_tests} test cases, removed {total_deleted} stale drafts, replaced {total_replaced} old bank questions, and reset {total_reset} assignments.",
            )
    return render(request, "faculty/question_upload.html", {"form": form, "results": results})


@login_required
def faculty_question_form(request, question_id=None):
    faculty_required(request.user)
    question = get_object_or_404(Question, pk=question_id) if question_id else None
    is_test_post = request.method == "POST" and request.POST.get("action") == "add_test"
    question_data = request.POST if request.method == "POST" and not is_test_post else None
    test_data = request.POST if is_test_post else None
    form = QuestionForm(question_data, instance=question)
    test_form = QuickTestCaseForm(test_data, initial={"order": 2})

    if is_test_post:
        if not question:
            messages.error(request, "Save the question before adding hidden tests.")
            return redirect("faculty_question_new")
        if test_form.is_valid():
            test = test_form.save(commit=False)
            test.question = question
            test.save()
            messages.success(request, "Test case added.")
            return redirect("faculty_question_edit", question.pk)
    elif request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        if not obj.created_by_id:
            obj.created_by = request.user
        obj.save()
        if obj.sample_output:
            TestCase.objects.update_or_create(
                question=obj,
                is_sample=True,
                order=1,
                defaults={"stdin": obj.sample_input, "expected_output": obj.sample_output},
            )
        messages.success(request, "Question saved.")
        return redirect("faculty_question_edit", obj.pk)
    tests = question.test_cases.all() if question else []
    return render(
        request,
        "faculty/question_form.html",
        {"form": form, "question": question, "tests": tests, "test_form": test_form},
    )


@login_required
def faculty_student_detail(request, student_id):
    """Faculty view showing a specific student's full dashboard."""
    faculty_required(request.user)
    student = get_object_or_404(User, pk=student_id)
    
    progress_rows = student_progress(student)
    modules = Module.objects.filter(is_active=True).prefetch_related("questions")
    progress_by_module = {row.module_id: row for row in progress_rows}
    user_submissions = Submission.objects.filter(student=student).values("question_id", "status")
    question_status_map = {}
    for sub in user_submissions:
        qid = sub["question_id"]
        st = sub["status"]
        if qid not in question_status_map:
            question_status_map[qid] = set()
        question_status_map[qid].add(st)
        
    all_subs = Submission.objects.filter(student=student).order_by('-submitted_at')
    latest_submissions = {}
    for sub in all_subs:
        if sub.question_id not in latest_submissions:
            latest_submissions[sub.question_id] = sub

    module_cards = []
    for module in modules:
        progress = progress_by_module.get(module.id)
        module_questions = module.questions.filter(is_active=True)
        module_total = min(15, module_questions.count())
        assigned_qs = AssignedQuestion.objects.filter(
            assignment__student=student, assignment__module=module
        )
        if assigned_qs.exists():
            module_completed = assigned_qs.filter(completed_at__isnull=False).count()
            questions_for_dots = [aq.question for aq in assigned_qs.select_related("question")]
        else:
            module_completed = module_questions.filter(
                submissions__student=student,
                submissions__status=Submission.Status.ACCEPTED,
            ).distinct().count()
            module_completed = min(module_completed, module_total)
            questions_for_dots = list(module_questions[:module_total])

        question_statuses = []
        questions_with_subs = []
        easy_questions = []
        medium_questions = []
        hard_questions = []
        
        for q in questions_for_dots:
            st_set = question_status_map.get(q.id, set())
            if Submission.Status.ACCEPTED in st_set:
                status_str = "completed"
                question_statuses.append("completed")
            elif any(
                s in st_set
                for s in [
                    Submission.Status.WRONG_ANSWER,
                    Submission.Status.TLE,
                    Submission.Status.RUNTIME_ERROR,
                    Submission.Status.COMPILE_ERROR,
                    Submission.Status.INTERNAL_ERROR,
                ]
            ):
                status_str = "failed"
                question_statuses.append("failed")
            else:
                status_str = "pending"
                question_statuses.append("pending")
                
            q_data = {
                "question": q,
                "status": status_str,
                "latest_submission": latest_submissions.get(q.id)
            }
            questions_with_subs.append(q_data)
            
            if q.difficulty == Question.Difficulty.EASY:
                easy_questions.append(q_data)
            elif q.difficulty == Question.Difficulty.MEDIUM:
                medium_questions.append(q_data)
            elif q.difficulty == Question.Difficulty.HARD:
                hard_questions.append(q_data)

        if not question_statuses and module_total > 0:
            question_statuses = ["pending"] * module_total

        module_percentage = (module_completed / module_total * 100) if module_total else 0
        module_cards.append(
            {
                "module": module,
                "progress": progress,
                "percentage": module_percentage,
                "module_total": module_total,
                "module_completed": module_completed,
                "completed": module_total > 0 and module_completed == module_total,
                "question_statuses": question_statuses,
                "questions_with_subs": questions_with_subs,
                "easy_questions": easy_questions,
                "medium_questions": medium_questions,
                "hard_questions": hard_questions,
            }
        )

    pct = overall_percentage(student)
    questions_total = sum(card["module_total"] for card in module_cards)
    completed_total = sum(card["module_completed"] for card in module_cards)
    eligible, _ = certificate_eligible(student)
    certificates = student.certificates.all()

    # Rank
    leaderboard_qs = (
        User.objects.filter(role=User.Role.STUDENT)
        .annotate(
            total_score=Coalesce(Sum("submissions__score"), Value(0)),
            problems_solved=Count("submissions__question", filter=Q(submissions__status=Submission.Status.ACCEPTED), distinct=True),
        )
    )
    try:
        current_user_stats = leaderboard_qs.get(id=student.id)
        user_rank = leaderboard_qs.filter(
            Q(total_score__gt=current_user_stats.total_score) |
            Q(total_score=current_user_stats.total_score, problems_solved__gt=current_user_stats.problems_solved) |
            Q(total_score=current_user_stats.total_score, problems_solved=current_user_stats.problems_solved, username__lt=current_user_stats.username)
        ).count() + 1
    except User.DoesNotExist:
        user_rank = None

    recent_activity = Submission.objects.filter(student=student).select_related("question", "question__module")[:10]
    return render(
        request,
        "faculty/student_detail.html",
        {
            "viewed_student": student,
            "modules": modules,
            "module_cards": module_cards,
            "progress_rows": progress_rows,
            "overall_percentage": pct,
            "questions_total": questions_total,
            "completed_total": completed_total,
            "not_attempted_total": max(questions_total - completed_total, 0),
            "certificate_eligible": eligible,
            "certificates": certificates,
            "user_rank": user_rank,
            "recent_activity": recent_activity,
            "existing_request": CertificateRequest.objects.filter(student=student).order_by("-updated_at").first(),
        },
    )


@login_required
def faculty_testcase_form(request, question_id):
    faculty_required(request.user)
    question = get_object_or_404(Question, pk=question_id)
    form = TestCaseForm(request.POST or None, initial={"question": question})
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Test case added.")
        return redirect("faculty_question_edit", question.pk)
    return render(request, "faculty/form.html", {"form": form, "title": "Test case"})


# =========================================================
#   Role Selection (HoD dual-login)
# =========================================================
@login_required
def role_select(request):
    if request.user.role != User.Role.HOD:
        return redirect("onboarding_overview")

    if request.method == "POST":
        chosen = request.POST.get("role", "faculty")
        if chosen in ("hod", "faculty"):
            request.session["active_role"] = chosen
        if chosen == "hod":
            return redirect("hod_dashboard")
        return redirect("onboarding_overview")

    return render(request, "registration/role_select.html")


# =========================================================
#   HoD Dashboard
# =========================================================
@login_required
def hod_dashboard(request):
    if request.user.role != User.Role.HOD or request.session.get("active_role") != "hod":
        return redirect("dashboard")

    pending_requests = CertificateRequest.objects.filter(
        status=CertificateRequest.Status.PENDING_HOD
    ).select_related("student", "requested_by_faculty").order_by("-updated_at")

    approved_count = CertificateRequest.objects.filter(status=CertificateRequest.Status.APPROVED).count()
    rejected_count = CertificateRequest.objects.filter(status=CertificateRequest.Status.REJECTED).count()
    total_students = User.objects.filter(role=User.Role.STUDENT).count()

    recent_decisions = CertificateRequest.objects.filter(
        status__in=[CertificateRequest.Status.APPROVED, CertificateRequest.Status.REJECTED]
    ).select_related("student", "requested_by_faculty", "approved_by_hod").order_by("-updated_at")[:10]

    return render(request, "hod/dashboard.html", {
        "pending_requests": pending_requests,
        "approved_count": approved_count,
        "rejected_count": rejected_count,
        "total_students": total_students,
        "recent_decisions": recent_decisions,
    })


# =========================================================
#   HoD Review Certificate Request
# =========================================================
@login_required
def hod_review_request(request, request_id):
    if request.user.role != User.Role.HOD or request.session.get("active_role") != "hod":
        return redirect("dashboard")

    cert_req = get_object_or_404(
        CertificateRequest.objects.select_related("student", "requested_by_faculty"),
        pk=request_id,
    )
    student = cert_req.student

    # Get full student activity
    modules = Module.objects.filter(is_active=True).prefetch_related("questions")
    module_progress = []
    for module in modules:
        total_q = min(15, module.questions.filter(is_active=True).count())
        solved = module.questions.filter(
            is_active=True,
            submissions__student=student,
            submissions__status=Submission.Status.ACCEPTED,
        ).distinct().count()
        solved = min(solved, total_q)
        pct = (solved / total_q * 100) if total_q else 0
        module_progress.append({
            "module": module,
            "total": total_q,
            "solved": solved,
            "percentage": pct,
        })

    recent_submissions = Submission.objects.filter(
        student=student
    ).select_related("question", "question__module").order_by("-submitted_at")[:30]

    pct = overall_percentage(student)

    return render(request, "hod/review_request.html", {
        "cert_req": cert_req,
        "student": student,
        "module_progress": module_progress,
        "recent_submissions": recent_submissions,
        "overall_pct": pct,
    })


# =========================================================
#   HoD Approve / Reject Certificate
# =========================================================
@login_required
@require_POST
def hod_approve_certificate(request, request_id):
    if request.user.role != User.Role.HOD or request.session.get("active_role") != "hod":
        raise PermissionDenied

    cert_req = get_object_or_404(CertificateRequest, pk=request_id, status=CertificateRequest.Status.PENDING_HOD)
    action = request.POST.get("action")
    notes = request.POST.get("notes", "").strip()

    if action == "approve":
        cert_req.status = CertificateRequest.Status.APPROVED
        cert_req.approved_by_hod = request.user
        cert_req.hod_notes = notes
        cert_req.save()
        # Auto-generate the certificate
        cert = generate_certificate(cert_req.student)
        notify_student_of_cert_decision(cert_req)
        messages.success(request, f"The certificate for {cert_req.student.display_name} has been approved!")
    elif action == "reject":
        cert_req.status = CertificateRequest.Status.REJECTED
        cert_req.approved_by_hod = request.user
        cert_req.hod_notes = notes
        cert_req.save()
        notify_student_of_cert_decision(cert_req)
        messages.info(request, f"Certificate request rejected for {cert_req.student.display_name}.")

    return redirect("hod_dashboard")


# =========================================================
#   Faculty Certificate Requests Page
# =========================================================
@login_required
def faculty_cert_requests(request):
    faculty_required(request.user)

    # Find students who have applied for certificate verification
    pending_reqs = CertificateRequest.objects.filter(
        status=CertificateRequest.Status.PENDING_FACULTY
    ).select_related("student").order_by("-updated_at")
    eligible_students = []
    for req in pending_reqs:
        _, pct = certificate_eligible(req.student)
        eligible_students.append({
            "student": req.student,
            "percentage": pct,
            "existing_request": req,
        })

    # Requests that this faculty has sent
    my_requests = CertificateRequest.objects.filter(
        requested_by_faculty=request.user
    ).select_related("student", "approved_by_hod").order_by("-updated_at")[:20]

    return render(request, "faculty/cert_requests.html", {
        "eligible_students": eligible_students,
        "my_requests": my_requests,
    })


# =========================================================
#   Faculty Send Certificate Request to HoD
# =========================================================
@login_required
@require_POST
def faculty_send_cert_request(request, student_id):
    faculty_required(request.user)

    student = get_object_or_404(User, pk=student_id, role=User.Role.STUDENT)
    is_eligible, pct = certificate_eligible(student)
    if not is_eligible:
        messages.error(request, f"{student.display_name} is not yet eligible for a certificate.")
        return redirect("faculty_cert_requests")

    # Check for existing pending request
    existing = CertificateRequest.objects.filter(
        student=student,
        status__in=[CertificateRequest.Status.PENDING_HOD, CertificateRequest.Status.APPROVED],
    ).first()
    if existing:
        messages.warning(request, f"A request for {student.display_name} already exists ({existing.get_status_display()}).")
        return redirect("faculty_cert_requests")

    notes = request.POST.get("notes", "").strip()
    cert_req = CertificateRequest.objects.create(
        student=student,
        requested_by_faculty=request.user,
        status=CertificateRequest.Status.PENDING_HOD,
        faculty_notes=notes,
        completion_percentage=pct,
    )
    notify_hod_of_cert_request(cert_req)
    messages.success(request, f"Approval request sent to HoD for {student.display_name}.")
    return redirect("faculty_cert_requests")


# =========================================================
#   Notifications
# =========================================================
@login_required
def notifications_list(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by("-created_at")[:50]
    return render(request, "notifications/list.html", {"notifications": notifications})


@login_required
def notification_mark_read(request, notification_id):
    notif = get_object_or_404(Notification, pk=notification_id, recipient=request.user)
    if not notif.is_read:
        notif.is_read = True
        notif.save(update_fields=["is_read"])
    if request.method == "GET" or request.POST.get("redirect") == "true" or request.GET.get("redirect") == "true":
        return redirect(notif.get_redirect_url)
    return redirect("notifications_list")


@login_required
@require_POST
def notifications_mark_all_read(request):
    Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
    return redirect("notifications_list")


class SubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Submission.objects.select_related("question", "student")
        if self.request.user.is_faculty_like:
            return qs
        return qs.filter(student=self.request.user)

    def create(self, request, *args, **kwargs):
        print("DEBUG: Request data:", request.data)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        print("DEBUG: Validated data:", serializer.validated_data)
        question = serializer.validated_data["question"]
        if not can_submit(self.request.user, question):
            raise PermissionDenied("Please wait 30 seconds before submitting again.")
            
        session_key = f"violations_{self.request.user.id}_{question.id}"
        violations = self.request.session.get(session_key, 0)
        self.request.session[session_key] = 0
        
        session_key_logs = f"violations_logs_{self.request.user.id}_{question.id}"
        logs = self.request.session.get(session_key_logs, [])
        self.request.session[session_key_logs] = []
        
        submission = serializer.save(
            student=self.request.user,
            language_id=question.language_id,
            status=Submission.Status.PENDING,
            proctoring_violations=violations,
            proctoring_logs=logs,
        )
        evaluate_submission_task.delay(submission.pk)


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.filter(is_active=True).select_related("module")


class ProgressViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        rows = student_progress(request.user)
        return Response(ProgressSerializer(rows, many=True).data)

    @action(detail=False, methods=["get"])
    def overall(self, request):
        eligible, pct = certificate_eligible(request.user)
        return Response({"percentage": pct, "certificate_eligible": eligible})


class SubmissionLatestViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=["get"])
    def latest(self, request):
        question_id = request.query_params.get("question_id")
        if not question_id:
            return Response({"submission": None}, status=400)

        qs = Submission.objects.select_related("question").filter(student=request.user, question_id=question_id)
        submission = qs.order_by("-id").first()
        if not submission:
            return Response({"submission": None}, status=200)

        data = SubmissionSerializer(submission).data
        # DRF serializer uses numeric statuses for `status`; frontend expects string.
        # We send both for safety.
        return Response({"submission": {**data, "status": submission.status, "status_display": submission.get_status_display()}})

@login_required
@require_POST
def report_violation(request):
    import json
    import datetime
    data = json.loads(request.body)
    question_id = data.get("question_id")
    reason = data.get("reason", "Unknown Violation")
    
    # Store count
    session_key_count = f"violations_{request.user.id}_{question_id}"
    violations = request.session.get(session_key_count, 0) + 1
    request.session[session_key_count] = violations
    
    # Store logs
    session_key_logs = f"violations_logs_{request.user.id}_{question_id}"
    logs = request.session.get(session_key_logs, [])
    timestamp = datetime.datetime.now().strftime("%I:%M:%S %p")
    logs.append(f"[{timestamp}] {reason}")
    request.session[session_key_logs] = logs
        
    return JsonResponse({"status": "logged", "violations": violations, "reason": reason})

@login_required
@require_POST
def faculty_send_note(request, student_id):
    if not request.user.is_faculty_like:
        raise PermissionDenied
    student = get_object_or_404(User, pk=student_id, role=User.Role.STUDENT)
    note = request.POST.get("note", "").strip()
    question_id = request.POST.get("question_id", "").strip()
    
    if note:
        title = f"Message from {request.user.display_name}"
        if question_id:
            try:
                question = Question.objects.get(pk=question_id)
                title = f"Message regarding: {question.title}"
            except Question.DoesNotExist:
                pass
                
        Notification.objects.create(
            recipient=student,
            notification_type=Notification.Type.FACULTY_NOTE,
            title=title,
            message=note,
            related_student=request.user,  # Using this field just to store who sent it
        )
        messages.success(request, f"Note sent to {student.display_name}.")
    return redirect("faculty_student_detail", student_id)

@login_required
def student_lab_record(request):
    if request.user.role != User.Role.STUDENT:
        raise PermissionDenied
        
    modules = Module.objects.filter(is_active=True).order_by("order").prefetch_related("questions")
    all_subs = Submission.objects.filter(
        student=request.user, 
        status=Submission.Status.ACCEPTED
    ).order_by("submitted_at").select_related("question")
    
    # Get the latest accepted submission per question
    latest_subs = {}
    for sub in all_subs:
        latest_subs[sub.question_id] = sub
        
    module_data = []
    for module in modules:
        qs = []
        for q in module.questions.filter(is_active=True).order_by("id"):
            if q.id in latest_subs:
                qs.append({
                    "question": q,
                    "submission": latest_subs[q.id]
                })
        if qs:
            module_data.append({
                "module": module,
                "questions": qs
            })
            
    return render(request, "student/lab_record.html", {"module_data": module_data})


@login_required
def profile_view(request):
    user = request.user
    profile_form = ProfileForm(request.POST or None, instance=user)
    password_form = PasswordChangeForm(user, request.POST or None if "change_password" in request.POST else None)

    # Set proper autocomplete attributes to prevent browser autofill conflicts
    if password_form:
        # Remove autofocus to prevent the old password field from auto-focusing on page load
        for field_name, field in password_form.fields.items():
            if 'password' in field_name:
                field.widget.attrs['autocomplete'] = 'current-password' if 'old' in field_name else 'new-password'
                field.widget.attrs.pop('autofocus', None)

    faculty_course_form = None
    if user.is_faculty_like:
        if request.method == "POST" and "update_courses" in request.POST:
            faculty_course_form = FacultyCourseSelectForm(request.POST)
            if faculty_course_form.is_valid():
                user.managed_courses.set(faculty_course_form.cleaned_data["courses"])
                messages.success(request, "Managed courses updated successfully.")
                return redirect("profile")
        else:
            faculty_course_form = FacultyCourseSelectForm(initial={"courses": user.managed_courses.all()})

    if request.method == "POST":
        if "update_profile" in request.POST:
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Profile updated successfully.")
                return redirect("profile")
        elif "change_password" in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Your password was successfully updated!")
                return redirect("profile")

    # User statistics
    total_submissions = Submission.objects.filter(student=user).count()
    accepted_submissions = Submission.objects.filter(student=user, status=Submission.Status.ACCEPTED).count()
    
    context = {
        "profile_form": profile_form,
        "password_form": password_form,
        "faculty_course_form": faculty_course_form,
        "total_submissions": total_submissions,
        "accepted_submissions": accepted_submissions,
    }
    return render(request, "registration/profile.html", context)


# --- Open-Ended Questions ---

@login_required
def student_open_ended_list(request):
    courses = get_faculty_modules(request.user).values_list('course', flat=True).distinct() if request.user.is_faculty_like else Course.objects.all()
    questions = OpenEndedQuestion.objects.filter(is_active=True).order_by('-assigned_date')
    return render(request, "student/open_ended_list.html", {"questions": questions})

@login_required
def faculty_open_ended_list(request):
    faculty_required(request.user)
    courses = request.user.managed_courses.all()
    questions = OpenEndedQuestion.objects.filter(course__in=courses).order_by('-assigned_date')
    return render(request, "faculty/open_ended_list.html", {"questions": questions})

@login_required
def faculty_open_ended_form(request, pk=None):
    faculty_required(request.user)
    question = get_object_or_404(OpenEndedQuestion, pk=pk) if pk else None
    
    # Check permissions
    if question and question.course not in request.user.managed_courses.all():
        raise PermissionDenied
        
    from .forms import OpenEndedQuestionForm
    form = OpenEndedQuestionForm(request.POST or None, instance=question)
    
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        if not obj.created_by_id:
            obj.created_by = request.user
        obj.save()
        messages.success(request, "Open-ended question saved.")
        return redirect("faculty_open_ended_list")
        
    return render(request, "faculty/open_ended_form.html", {"form": form, "question": question})

@login_required
@require_POST
def faculty_open_ended_delete(request, pk):
    faculty_required(request.user)
    question = get_object_or_404(OpenEndedQuestion, pk=pk)
    if question.course not in request.user.managed_courses.all():
        raise PermissionDenied
    question.delete()
    messages.success(request, "Question deleted.")
    return redirect("faculty_open_ended_list")

# --- Quizzes ---

@login_required
def student_quiz_list(request):
    quizzes = Quiz.objects.filter(is_active=True).order_by('-created_at')
    return render(request, "student/quiz_list.html", {"quizzes": quizzes})

@login_required
def student_quiz_take(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, is_active=True)
    if not quiz.is_open:
        messages.error(request, "This quiz is not currently open.")
        return redirect("student_quiz_list")
        
    attempt, created = QuizAttempt.objects.get_or_create(
        quiz=quiz,
        student=request.user,
        defaults={"max_score": quiz.total_points}
    )
    
    if attempt.finished_at or attempt.is_timed_out:
        messages.info(request, "You have already completed this quiz.")
        return redirect("student_quiz_results", quiz_id=quiz.id)
        
    # Simplified version for now
    questions = quiz.quiz_questions.select_related('question').order_by('order')
    return render(request, "student/quiz_take.html", {"quiz": quiz, "attempt": attempt, "questions": questions})

@login_required
def student_quiz_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    attempt = get_object_or_404(QuizAttempt, quiz=quiz, student=request.user)
    
    if not quiz.show_results:
        messages.info(request, "Results are currently hidden by the instructor.")
        return redirect("student_quiz_list")
        
    return render(request, "student/quiz_results.html", {"quiz": quiz, "attempt": attempt})

@login_required
def faculty_quiz_list(request):
    faculty_required(request.user)
    quizzes = Quiz.objects.filter(course__in=request.user.managed_courses.all()).order_by('-created_at')
    return render(request, "faculty/quiz_list.html", {"quizzes": quizzes})

@login_required
def faculty_quiz_form(request, quiz_id=None):
    faculty_required(request.user)
    quiz = get_object_or_404(Quiz, pk=quiz_id) if quiz_id else None
    
    if quiz and quiz.course not in request.user.managed_courses.all():
        raise PermissionDenied
        
    from .forms import QuizForm
    form = QuizForm(request.POST or None, instance=quiz)
    
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        if not obj.created_by_id:
            obj.created_by = request.user
        obj.save()
        messages.success(request, "Quiz saved.")
        return redirect("faculty_quiz_detail", quiz_id=obj.id)
        
    return render(request, "faculty/quiz_form.html", {"form": form, "quiz": quiz})

@login_required
def faculty_quiz_detail(request, quiz_id):
    faculty_required(request.user)
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    
    if quiz.course not in request.user.managed_courses.all():
        raise PermissionDenied
        
    attempts = quiz.attempts.select_related('student').order_by('-total_score')
    return render(request, "faculty/quiz_detail.html", {"quiz": quiz, "attempts": attempts})

@login_required
@require_POST
def faculty_quiz_toggle(request, quiz_id):
    faculty_required(request.user)
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if quiz.course not in request.user.managed_courses.all():
        raise PermissionDenied
        
    quiz.is_active = not quiz.is_active
    quiz.save()
    messages.success(request, f"Quiz is now {'active' if quiz.is_active else 'inactive'}.")
    return redirect("faculty_quiz_detail", quiz_id=quiz.id)

@login_required
def faculty_quiz_upload(request):
    faculty_required(request.user)
    messages.info(request, "Question upload for quizzes is coming soon.")
    return redirect("faculty_quiz_list")


# ─── FACULTY RAG AGENT API ENDPOINTS ───

from django.http import JsonResponse
from django.utils.text import slugify
from .rag_agent import RAGQuestionAgent


def _parse_agent_request_data(request):
    """Robustly parse JSON body or POST form data."""
    cached = getattr(request, "_parsed_agent_data", None)
    if cached:
        return cached

    data = {}
    try:
        raw_text = request.body.decode("utf-8")
        if raw_text.strip():
            data = json.loads(raw_text)
    except Exception:
        pass


    if not data and request.POST:
        data = request.POST.dict()

    request._parsed_agent_data = data
    return data




@login_required
def faculty_agent_topics_api(request):
    """Return modules and RAG topics for faculty agent autocomplete."""
    if not request.user.is_faculty_like:
        return JsonResponse({"error": "Faculty access required"}, status=403)

    modules = list(
        Module.objects.filter(is_active=True)
        .select_related("course")
        .values("id", "name", "level", "course__name")
    )
    
    agent = RAGQuestionAgent.get_instance()
    topics = agent.list_topics()

    return JsonResponse({
        "modules": modules,
        "topics": topics
    })


@login_required
@require_POST
def faculty_agent_generate_api(request):
    """Generate a new question via RAG agent based on faculty prompt."""
    if not request.user.is_faculty_like:
        return JsonResponse({"error": "Faculty access required"}, status=403)

    data = _parse_agent_request_data(request)

    topic = str(data.get("topic", "array")).strip()
    difficulty = str(data.get("difficulty", "medium")).strip()
    custom_prompt = str(data.get("prompt", "")).strip()

    if not topic:
        return JsonResponse({"error": "Topic is required"}, status=400)

    try:
        agent = RAGQuestionAgent.get_instance()
        result, references = agent.generate_question(topic, difficulty, custom_prompt)
        
        ref_summary = [
            {"title": r.get("title", ""), "topic": r.get("topic", ""), "difficulty": r.get("difficulty", "")}
            for r in references
        ]

        return JsonResponse({
            "success": True,
            "question": result,
            "references": ref_summary
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
@require_POST
def faculty_agent_add_question_api(request):
    """Add generated question directly into E-Lab Question Bank."""
    if not request.user.is_faculty_like:
        return JsonResponse({"error": "Faculty access required"}, status=403)

    data = _parse_agent_request_data(request)

    module_id = data.get("module_id")
    title = str(data.get("title", "")).strip()
    description = str(data.get("description", "")).strip()
    difficulty = str(data.get("difficulty", Question.Difficulty.MEDIUM)).lower()
    starter_code = str(data.get("starter_code", "")).strip()
    test_cases_data = data.get("test_cases", [])

    if module_id is None or module_id == "" or not title or not description:
        return JsonResponse({"error": "Module, title, and description are required", "received_keys": list(data.keys())}, status=400)

    try:
        module = Module.objects.get(pk=int(module_id))
    except (Module.DoesNotExist, ValueError, TypeError):
        return JsonResponse({"error": f"Invalid module_id: {module_id}"}, status=400)

    # Generate unique slug for module
    base_slug = slugify(title) or "question"
    slug = base_slug
    counter = 1
    while Question.objects.filter(module=module, slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    valid_difficulty = (
        difficulty if difficulty in [Question.Difficulty.EASY, Question.Difficulty.MEDIUM, Question.Difficulty.HARD]
        else Question.Difficulty.MEDIUM
    )

    # Extract sample input/output from first testcase if available
    sample_input = ""
    sample_output = ""
    if isinstance(test_cases_data, list):
        for tc in test_cases_data:
            if isinstance(tc, dict) and tc.get("is_sample"):
                sample_input = str(tc.get("input", ""))
                sample_output = str(tc.get("expected_output", ""))
                break

    # Default starter code for C if blank
    if not starter_code:
        starter_code = "#include <stdio.h>\n\nint main() {\n    // Write your solution here\n    return 0;\n}"

    question = Question.objects.create(
        module=module,
        title=title,
        slug=slug,
        description=description,
        difficulty=valid_difficulty,
        sample_input=sample_input,
        sample_output=sample_output,
        starter_code=starter_code,
        created_by=request.user,
        is_mandatory=True,
        is_active=True
    )

    # Add Test Cases
    if isinstance(test_cases_data, list):
        for index, tc in enumerate(test_cases_data, 1):
            if not isinstance(tc, dict):
                continue
            stdin_val = str(tc.get("input", ""))
            expected_val = str(tc.get("expected_output", ""))
            is_samp = bool(tc.get("is_sample", False))
            
            TestCase.objects.create(
                question=question,
                stdin=stdin_val,
                expected_output=expected_val,
                is_sample=is_samp,
                order=index
            )

    from django.urls import reverse
    url = reverse("question_detail", args=[question.pk])
    edit_url = reverse("faculty_question_edit", args=[question.pk])

    return JsonResponse({
        "success": True,
        "message": f"Question '{question.title}' added successfully to {module.name}!",
        "question_id": question.pk,
        "question_url": url,
        "edit_url": edit_url
    })





