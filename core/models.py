import hmac
import hashlib
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        FACULTY = "faculty", "Faculty"
        HOD = "hod", "HoD"
        ADMIN = "admin", "Admin"

    usn = models.CharField(max_length=32, blank=True, unique=True, null=True)
    role = models.CharField(max_length=16, choices=Role.choices, default=Role.STUDENT)
    department = models.CharField(max_length=80, blank=True)
    semester = models.PositiveSmallIntegerField(default=1)
    bio = models.TextField(blank=True, max_length=500)
    managed_modules = models.ManyToManyField(
        "Module",
        blank=True,
        related_name="managing_faculty",
        help_text="Deprecated — use managed_courses instead.",
    )
    managed_courses = models.ManyToManyField(
        "Course",
        blank=True,
        related_name="managing_faculty",
        help_text="Courses this faculty member manages (faculty/HoD only).",
    )

    @property
    def display_name(self):
        return self.get_full_name() or self.username

    @property
    def initials(self):
        """Return up to 2 initials for avatar display."""
        name = self.get_full_name()
        if name:
            parts = name.split()
            if len(parts) >= 2:
                return (parts[0][0] + parts[-1][0]).upper()
            return parts[0][0].upper()
        return self.username[0].upper()

    @property
    def is_faculty_like(self):
        if self.role == self.Role.STUDENT:
            return False
        return self.role in {self.Role.FACULTY, self.Role.HOD, self.Role.ADMIN} or self.is_staff

    @property
    def is_hod(self):
        return self.role == self.Role.HOD


class Course(models.Model):
    """Top-level course that groups modules (e.g. 'C Programming', 'Python')."""
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True)
    year = models.PositiveSmallIntegerField(default=1, help_text="Target year (1st, 2nd, etc.)")
    semester = models.PositiveSmallIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["year", "name"]

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    level = models.PositiveSmallIntegerField(default=1)
    order = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    category = models.CharField(max_length=50, default="c_programming")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="modules",
        null=True, blank=True,
        help_text="The course this module belongs to.",
    )

    class Meta:
        ordering = ["order", "level", "name"]

    def __str__(self):
        return self.name


class Question(models.Model):
    class Difficulty(models.TextChoices):
        EASY = "easy", "Easy"
        MEDIUM = "medium", "Medium"
        HARD = "hard", "Hard"

    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180)
    description = models.TextField()
    difficulty = models.CharField(max_length=16, choices=Difficulty.choices, default=Difficulty.EASY)
    csv_level = models.PositiveSmallIntegerField(default=1)
    level_range = models.CharField(max_length=32, blank=True)
    sample_input = models.TextField(blank=True)
    sample_output = models.TextField(blank=True)
    starter_code = models.TextField(blank=True)
    language_id = models.PositiveIntegerField(default=50, help_text="Language id. 50 is C (GCC).")
    time_limit = models.FloatField(default=2.0)
    memory_limit_kb = models.PositiveIntegerField(default=128000)
    allow_multiple_languages = models.BooleanField(default=False)
    starter_codes = models.JSONField(default=dict, blank=True)
    is_mandatory = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["module__order", "title"]
        unique_together = [("module", "slug")]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("question_detail", args=[self.pk])


class TestCase(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="test_cases")
    stdin = models.TextField(blank=True)
    expected_output = models.TextField()
    is_sample = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        label = "sample" if self.is_sample else "hidden"
        return f"{self.question} ({label} #{self.order})"


class Submission(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        RUNNING = "running", "Running"
        ACCEPTED = "accepted", "Accepted"
        WRONG_ANSWER = "wrong_answer", "Wrong Answer"
        TLE = "tle", "Time Limit Exceeded"
        COMPILE_ERROR = "compile_error", "Compilation Error"
        RUNTIME_ERROR = "runtime_error", "Runtime Error"
        INTERNAL_ERROR = "internal_error", "Internal Error"

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="submissions")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="submissions")
    code = models.TextField()
    language_id = models.PositiveIntegerField(default=50)
    status = models.CharField(max_length=32, choices=Status.choices, default=Status.PENDING)
    score = models.PositiveSmallIntegerField(default=0)
    execution_time = models.FloatField(null=True, blank=True)
    memory_used = models.PositiveIntegerField(null=True, blank=True)
    judge_output = models.TextField(blank=True)
    error_output = models.TextField(blank=True)
    manually_graded = models.BooleanField(default=False)
    graded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="graded_submissions",
    )
    proctoring_violations = models.PositiveIntegerField(default=0)
    proctoring_logs = models.JSONField(default=list)
    submitted_at = models.DateTimeField(auto_now_add=True)
    judged_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.student} - {self.question} - {self.status}"


class LabSession(models.Model):
    date = models.DateField(default=timezone.localdate)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="lab_sessions")
    students_present = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="lab_sessions_present")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "module__order"]
        unique_together = [("date", "module")]

    def __str__(self):
        return f"{self.module} - {self.date}"


class Attendance(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="attendance_rows")
    session = models.ForeignKey(LabSession, on_delete=models.CASCADE, related_name="attendance_rows")
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    time_spent_minutes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-login_time"]
        unique_together = [("student", "session", "login_time")]

    def __str__(self):
        return f"{self.student} - {self.session}"


class ModuleQuestionAssignment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="module_assignments")
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="question_assignments")
    difficulty = models.CharField(max_length=16, choices=Question.Difficulty.choices, default=Question.Difficulty.EASY)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = [("student", "module", "difficulty")]
        ordering = ["module__order", "difficulty", "created_at"]

    def __str__(self):
        return f"{self.student} - {self.module}"


class AssignedQuestion(models.Model):
    assignment = models.ForeignKey(ModuleQuestionAssignment, on_delete=models.CASCADE, related_name="assigned_questions")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="assigned_slots")
    order = models.PositiveSmallIntegerField()
    unlocked_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["order"]
        unique_together = [("assignment", "question"), ("assignment", "order")]

    def __str__(self):
        return f"{self.assignment} #{self.order}"


class Progress(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="progress_rows")
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="progress_rows")
    attempted = models.PositiveIntegerField(default=0)
    completed = models.PositiveIntegerField(default=0)
    percentage = models.FloatField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [("student", "module")]
        ordering = ["module__order"]

    def __str__(self):
        return f"{self.student} - {self.module}: {self.percentage:.0f}%"


class Certificate(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="certificates")
    semester = models.CharField(max_length=32)
    completion_percentage = models.FloatField()
    verification_hash = models.CharField(max_length=96, unique=True)
    pdf = models.FileField(upload_to="certificates/pdf/", blank=True)
    qr_code = models.ImageField(upload_to="certificates/qr/", blank=True)
    issued_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-issued_at"]

    def __str__(self):
        return f"{self.student} - {self.semester}"

    @classmethod
    def make_hash(cls, student, semester, percentage):
        data = f"{student.pk}:{student.usn}:{semester}:{percentage:.2f}"
        return hmac.new(
            settings.CERTIFICATE_SIGNING_KEY.encode(),
            data.encode(),
            hashlib.sha256,
        ).hexdigest()

    @classmethod
    def current_semester_label(cls):
        now = timezone.localtime()
        term = "Odd" if now.month >= 7 else "Even"
        return f"{now.year}-{str(now.year + 1)[-2:]} {term}"


class Notification(models.Model):
    class Type(models.TextChoices):
        CERT_ELIGIBLE = "cert_eligible", "Student Certificate Eligible"
        CERT_FACULTY_REQUEST = "cert_faculty_request", "Faculty Sent Approval Request"
        CERT_HOD_APPROVED = "cert_hod_approved", "HoD Approved Certificate"
        CERT_HOD_REJECTED = "cert_hod_rejected", "HoD Rejected Certificate"
        FACULTY_NOTE = "faculty_note", "Message from Faculty"

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications"
    )
    notification_type = models.CharField(max_length=32, choices=Type.choices)
    title = models.CharField(max_length=200)
    message = models.TextField()
    related_student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        null=True, blank=True, related_name="+"
    )
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.recipient} — {self.title}"

    @property
    def get_redirect_url(self):
        from django.urls import reverse
        if self.notification_type == self.Type.CERT_ELIGIBLE:
            if self.related_student:
                return reverse("faculty_student_detail", args=[self.related_student.id])
            return reverse("faculty_cert_requests")
        elif self.notification_type == self.Type.CERT_FACULTY_REQUEST:
            if self.related_student:
                req = CertificateRequest.objects.filter(
                    student=self.related_student,
                    status=CertificateRequest.Status.PENDING_HOD
                ).order_by("-updated_at").first()
                if not req:
                    req = CertificateRequest.objects.filter(student=self.related_student).order_by("-updated_at").first()
                if req:
                    return reverse("hod_review_request", args=[req.id])
            return reverse("hod_dashboard")
        elif self.notification_type in [self.Type.CERT_HOD_APPROVED, self.Type.CERT_HOD_REJECTED]:
            return reverse("dashboard")
        return reverse("notifications_list")

    @property
    def cert_action_state(self):
        from django.urls import reverse
        if self.notification_type not in [self.Type.CERT_ELIGIBLE, self.Type.CERT_FACULTY_REQUEST, self.Type.CERT_HOD_APPROVED, self.Type.CERT_HOD_REJECTED]:
            return None
        if not self.related_student:
            return None
        req = CertificateRequest.objects.filter(student=self.related_student).order_by("-updated_at").first()
        if not req:
            return None

        if self.recipient.role == "faculty":
            if req.status == CertificateRequest.Status.PENDING_FACULTY:
                return {"label": "Review & Forward ➔", "open": True, "url": reverse("faculty_student_detail", args=[self.related_student.id])}
            elif req.status == CertificateRequest.Status.PENDING_HOD:
                return {"label": "⏳ Req Already Sent to HoD", "open": False, "url": "#"}
            elif req.status == CertificateRequest.Status.APPROVED:
                return {"label": "✅ Certificate Approved", "open": False, "url": "#"}
            elif req.status == CertificateRequest.Status.REJECTED:
                return {"label": "❌ Request Declined", "open": False, "url": "#"}

        elif self.recipient.role == "hod":
            if req.status == CertificateRequest.Status.PENDING_HOD:
                return {"label": "Authorize & Issue ➔", "open": True, "url": reverse("hod_review_request", args=[req.id])}
            elif req.status == CertificateRequest.Status.APPROVED:
                return {"label": "✅ Already Approved by HoD", "open": False, "url": "#"}
            elif req.status == CertificateRequest.Status.REJECTED:
                return {"label": "❌ Already Declined by HoD", "open": False, "url": "#"}
            else:
                return {"label": f"⏳ {req.get_status_display()}", "open": False, "url": "#"}

        elif self.recipient.role == "student":
            if req.status == CertificateRequest.Status.APPROVED:
                cert = Certificate.objects.filter(student=self.related_student).first()
                url = reverse("certificate_detail", args=[cert.id]) if cert else reverse("certificate_create")
                return {"label": "📥 View Diploma ↗", "open": True, "url": url}
            elif req.status == CertificateRequest.Status.REJECTED:
                return {"label": "❌ Request Declined", "open": False, "url": "#"}
            else:
                return {"label": "⏳ Under Review", "open": False, "url": "#"}

        return None


class CertificateRequest(models.Model):
    class Status(models.TextChoices):
        PENDING_FACULTY = "pending_faculty", "Awaiting Faculty Review"
        PENDING_HOD = "pending_hod", "Awaiting HoD Approval"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="certificate_requests"
    )
    requested_by_faculty = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="faculty_cert_requests"
    )
    approved_by_hod = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="hod_cert_approvals"
    )
    status = models.CharField(
        max_length=32, choices=Status.choices, default=Status.PENDING_FACULTY
    )
    faculty_notes = models.TextField(blank=True)
    hod_notes = models.TextField(blank=True)
    completion_percentage = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.student} — {self.get_status_display()}"


class OpenEndedQuestion(models.Model):
    """Take-home question students write answers for in a physical notebook."""
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="open_ended_questions",
        null=True, blank=True,
    )
    title = models.CharField(max_length=200)
    description = models.TextField(
        help_text="Full question text. Students will see this on-screen and write answers in their books.",
    )
    assigned_date = models.DateField(default=timezone.localdate)
    due_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="created_open_ended",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-assigned_date", "-created_at"]

    def __str__(self):
        return self.title


class Quiz(models.Model):
    """A timed quiz/test that faculty can create on-demand."""
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="quizzes",
        null=True, blank=True,
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name="created_quizzes",
    )
    duration_minutes = models.PositiveIntegerField(default=60)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    show_results = models.BooleanField(
        default=True,
        help_text="Whether students can see results after completing the quiz.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "quizzes"

    def __str__(self):
        return self.title

    @property
    def is_open(self):
        now = timezone.now()
        if not self.is_active:
            return False
        if self.start_time and now < self.start_time:
            return False
        if self.end_time and now > self.end_time:
            return False
        return True

    @property
    def question_count(self):
        return self.quiz_questions.count()

    @property
    def total_points(self):
        return sum(qq.points for qq in self.quiz_questions.all())


class QuizQuestion(models.Model):
    """Through-model linking a Quiz to a Question with ordering and points."""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="quiz_questions")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="quiz_slots")
    order = models.PositiveSmallIntegerField(default=1)
    points = models.PositiveSmallIntegerField(default=10)

    class Meta:
        ordering = ["order"]
        unique_together = [("quiz", "question"), ("quiz", "order")]

    def __str__(self):
        return f"{self.quiz} — Q{self.order}: {self.question}"


class QuizAttempt(models.Model):
    """A student's attempt at a quiz."""
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="attempts")
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="quiz_attempts",
    )
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    total_score = models.PositiveIntegerField(default=0)
    max_score = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-started_at"]
        unique_together = [("quiz", "student")]

    def __str__(self):
        return f"{self.student} — {self.quiz}"

    @property
    def percentage(self):
        return (self.total_score / self.max_score * 100) if self.max_score else 0

    @property
    def is_timed_out(self):
        if not self.finished_at and self.quiz.duration_minutes:
            from datetime import timedelta
            deadline = self.started_at + timedelta(minutes=self.quiz.duration_minutes)
            return timezone.now() > deadline
        return False
