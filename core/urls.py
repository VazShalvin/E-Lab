from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("submissions", views.SubmissionViewSet, basename="submission")
router.register("questions", views.QuestionViewSet, basename="question-api")
router.register("progress", views.ProgressViewSet, basename="progress")
router.register("submission-latest", views.SubmissionLatestViewSet, basename="submission-latest")

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("login/", views.AppLoginView.as_view(), name="login"),
    path("logout/", views.AppLogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("profile/", views.profile_view, name="profile"),
    path("role-select/", views.role_select, name="role_select"),
    path("overview/", views.onboarding_overview, name="onboarding_overview"),
    path("about/", views.about, name="about"),
    path("course-selection/", views.onboarding_journey, name="onboarding_journey"),
    path("placement-training/overview/", views.placement_training_overview, name="placement_training_overview"),
    path("modules/<int:module_id>/", views.module_detail, name="module_detail"),
    path("modules/<int:module_id>/<str:difficulty>/", views.module_level_detail, name="module_level_detail"),
    path("questions/<int:question_id>/", views.question_detail, name="question_detail"),
    path("submissions/<int:submission_id>/", views.submission_detail, name="submission_detail"),
    path("submissions/<int:submission_id>/manual-accept/", views.manual_accept_submission, name="manual_accept_submission"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("certificates/generate/", views.certificate_create, name="certificate_create"),
    path("certificates/<int:certificate_id>/", views.certificate_detail, name="certificate_detail"),
    path("verify/<str:verification_hash>/", views.certificate_verify, name="certificate_verify"),
    path("lab-record/", views.student_lab_record, name="student_lab_record"),
    path("open-ended/", views.student_open_ended_list, name="student_open_ended_list"),
    path("quizzes/", views.student_quiz_list, name="student_quiz_list"),
    path("quizzes/<int:quiz_id>/", views.student_quiz_take, name="student_quiz_take"),
    path("quizzes/<int:quiz_id>/results/", views.student_quiz_results, name="student_quiz_results"),
    # HoD routes
    path("hod/", views.hod_dashboard, name="hod_dashboard"),
    path("hod/requests/<int:request_id>/", views.hod_review_request, name="hod_review_request"),
    path("hod/requests/<int:request_id>/approve/", views.hod_approve_certificate, name="hod_approve_certificate"),
    # Faculty routes
    path("faculty/cert-requests/", views.faculty_cert_requests, name="faculty_cert_requests"),
    path("faculty/cert-requests/send/<int:student_id>/", views.faculty_send_cert_request, name="faculty_send_cert_request"),
    path("faculty/attendance/", views.attendance_report, name="attendance_report"),
    path("faculty/export/progress/", views.export_progress, name="export_progress"),
    path("faculty/modules/new/", views.faculty_module_form, name="faculty_module_new"),
    path("faculty/modules/<int:module_id>/", views.faculty_module_form, name="faculty_module_edit"),
    path("faculty/modules/<int:module_id>/delete/", views.faculty_module_delete, name="faculty_module_delete"),
    path("faculty/question-bank/", views.faculty_question_bank, name="faculty_question_bank"),
    path("faculty/question-bank/<int:module_id>/", views.faculty_question_bank, name="faculty_question_bank_module"),
    path("faculty/questions/upload/", views.faculty_question_upload, name="faculty_question_upload"),
    path("faculty/questions/upload/demo/<str:file_type>/", views.download_demo_file, name="download_demo_file"),
    path("faculty/questions/new/", views.faculty_question_form, name="faculty_question_new"),
    path("faculty/questions/<int:question_id>/", views.faculty_question_form, name="faculty_question_edit"),
    path("faculty/student/<int:student_id>/", views.faculty_student_detail, name="faculty_student_detail"),
    path("faculty/student/<int:student_id>/note/", views.faculty_send_note, name="faculty_send_note"),
    path("faculty/questions/<int:question_id>/tests/new/", views.faculty_testcase_form, name="faculty_testcase_new"),
    path("faculty/open-ended/", views.faculty_open_ended_list, name="faculty_open_ended_list"),
    path("faculty/open-ended/new/", views.faculty_open_ended_form, name="faculty_open_ended_new"),
    path("faculty/open-ended/<int:pk>/edit/", views.faculty_open_ended_form, name="faculty_open_ended_edit"),
    path("faculty/open-ended/<int:pk>/delete/", views.faculty_open_ended_delete, name="faculty_open_ended_delete"),
    path("faculty/quizzes/", views.faculty_quiz_list, name="faculty_quiz_list"),
    path("faculty/quizzes/new/", views.faculty_quiz_form, name="faculty_quiz_new"),
    path("faculty/quizzes/<int:quiz_id>/", views.faculty_quiz_detail, name="faculty_quiz_detail"),
    path("faculty/quizzes/<int:quiz_id>/edit/", views.faculty_quiz_form, name="faculty_quiz_edit"),
    path("faculty/quizzes/<int:quiz_id>/toggle/", views.faculty_quiz_toggle, name="faculty_quiz_toggle"),
    path("faculty/quizzes/upload-questions/", views.faculty_quiz_upload, name="faculty_quiz_upload"),
    # Notifications
    path("notifications/", views.notifications_list, name="notifications_list"),
    path("notifications/<int:notification_id>/read/", views.notification_mark_read, name="notification_mark_read"),
    path("notifications/mark-all-read/", views.notifications_mark_all_read, name="notifications_mark_all_read"),
    # Misc
    path("health/", views.health_check, name="health_check"),
    path("api/run/", views.run_code_api, name="run-code"),
    path("api/report-violation/", views.report_violation, name="report_violation"),
    # Faculty Agent Routes
    path("api/faculty-agent/topics/", views.faculty_agent_topics_api, name="faculty_agent_topics_api"),
    path("api/faculty-agent/generate/", views.faculty_agent_generate_api, name="faculty_agent_generate_api"),
    path("api/faculty-agent/add-question/", views.faculty_agent_add_question_api, name="faculty_agent_add_question_api"),
    path("api/", include(router.urls)),
]

