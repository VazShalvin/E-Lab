from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    AssignedQuestion,
    Attendance,
    Certificate,
    CertificateRequest,
    Course,
    LabSession,
    Module,
    ModuleQuestionAssignment,
    Notification,
    OpenEndedQuestion,
    Progress,
    Question,
    Quiz,
    QuizAttempt,
    QuizQuestion,
    StudentQuestionHint,
    Submission,
    TestCase,
    User,
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("e-Lab profile", {"fields": ("usn", "role", "department", "semester", "bio", "managed_modules", "managed_courses")}),
    )
    list_display = ("username", "email", "usn", "role", "department", "semester", "is_staff")
    list_filter = ("role", "department", "semester", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name", "usn")
    filter_horizontal = ("managed_modules", "managed_courses")


class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "year", "semester", "proctoring_enabled", "is_active")
    list_filter = ("year", "proctoring_enabled", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "difficulty", "language_id", "is_mandatory", "proctoring_enabled", "is_active")
    list_filter = ("module", "difficulty", "is_mandatory", "proctoring_enabled", "is_active")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [TestCaseInline]


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "question",
        "status",
        "score",
        "manually_graded",
        "submitted_at",
        "judged_at",
    )
    list_filter = ("status", "question__module", "manually_graded")
    search_fields = ("student__username", "student__usn", "question__title")


@admin.register(LabSession)
class LabSessionAdmin(admin.ModelAdmin):
    list_display = ("date", "module", "present_count", "created_at")
    list_filter = ("date", "module")
    filter_horizontal = ("students_present",)

    def present_count(self, obj):
        return obj.students_present.count()


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("student", "session", "login_time", "logout_time", "time_spent_minutes")
    list_filter = ("session__date", "session__module")
    search_fields = ("student__username", "student__usn", "student__first_name", "student__last_name")


class AssignedQuestionInline(admin.TabularInline):
    model = AssignedQuestion
    extra = 0


@admin.register(ModuleQuestionAssignment)
class ModuleQuestionAssignmentAdmin(admin.ModelAdmin):
    list_display = ("student", "module", "created_at", "completed_at")
    list_filter = ("module", "completed_at")
    search_fields = ("student__username", "student__usn", "module__name")
    inlines = [AssignedQuestionInline]


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ("student", "module", "attempted", "completed", "percentage", "updated_at")
    list_filter = ("module",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "completion_percentage", "issued_at")
    search_fields = ("student__username", "student__usn", "verification_hash")


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("recipient", "notification_type", "title", "is_read", "created_at")
    list_filter = ("notification_type", "is_read")
    search_fields = ("recipient__username", "title")


@admin.register(CertificateRequest)
class CertificateRequestAdmin(admin.ModelAdmin):
    list_display = ("student", "status", "requested_by_faculty", "approved_by_hod", "completion_percentage", "updated_at")
    list_filter = ("status",)
    search_fields = ("student__username", "student__usn")


@admin.register(OpenEndedQuestion)
class OpenEndedQuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "assigned_date", "due_date", "is_active")
    list_filter = ("course", "is_active", "assigned_date")
    search_fields = ("title", "description")


class QuizQuestionInline(admin.TabularInline):
    model = QuizQuestion
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "duration_minutes", "start_time", "end_time", "is_active")
    list_filter = ("course", "is_active")
    search_fields = ("title", "description")
    inlines = [QuizQuestionInline]


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ("student", "quiz", "started_at", "finished_at", "total_score")
    list_filter = ("quiz",)
    search_fields = ("student__username", "student__usn")


@admin.register(StudentQuestionHint)
class StudentQuestionHintAdmin(admin.ModelAdmin):
    list_display = ("student", "question", "hint_number", "hint_type", "unlocked_at")
    list_filter = ("hint_number", "hint_type")
    search_fields = ("student__username", "student__usn", "question__title")


