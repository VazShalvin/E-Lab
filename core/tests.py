from unittest.mock import patch

from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse

from .models import User


class DashboardRoutingTests(TestCase):
    def test_admin_is_sent_to_admin_dashboard(self):
        admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="password123",
            role=User.Role.ADMIN,
        )
        self.client.force_login(admin)

        response = self.client.get(reverse("dashboard"))

        self.assertRedirects(response, reverse("admin:index"), fetch_redirect_response=False)

    def test_faculty_still_sees_faculty_dashboard(self):
        faculty = User.objects.create_user(
            username="faculty",
            password="password123",
            role=User.Role.FACULTY,
        )
        self.client.force_login(faculty)

        with patch("core.views.render", return_value=HttpResponse()) as render_mock:
            response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(render_mock.call_args.args[1], "faculty/dashboard.html")


class HintSystemTests(TestCase):
    def setUp(self):
        from .models import Course, Module, Question
        self.student = User.objects.create_user(
            username="test_student",
            password="password123",
            role=User.Role.STUDENT,
        )
        self.course = Course.objects.create(name="C Programming", slug="c-programming")
        self.module = Module.objects.create(name="Module 1", course=self.course, order=1)
        self.question = Question.objects.create(
            title="Sum of Two Numbers",
            slug="sum-of-two",
            module=self.module,
            description="Given two integers, print their sum.",
            difficulty=Question.Difficulty.EASY,
        )

    def test_progressive_hints_capped_at_three(self):
        from .hint_service import generate_hint_for_submission, get_student_hints_for_question
        from .models import StudentQuestionHint, Submission

        # 1st unsuccessful submission
        sub1 = Submission.objects.create(
            student=self.student,
            question=self.question,
            code="int main() { return 0; }",
            status=Submission.Status.WRONG_ANSWER,
            judge_output='[{"passed": false, "stdin": "2 3", "expected": "5", "actual": "0"}]',
        )
        h1 = generate_hint_for_submission(sub1)
        self.assertIsNotNone(h1)
        self.assertEqual(h1.hint_number, 1)
        self.assertTrue(len(h1.hint_text) > 10)

        # 2nd unsuccessful submission
        sub2 = Submission.objects.create(
            student=self.student,
            question=self.question,
            code="int main() { while(1); }",
            status=Submission.Status.TLE,
            error_output="Time Limit Exceeded",
        )
        h2 = generate_hint_for_submission(sub2)
        self.assertIsNotNone(h2)
        self.assertEqual(h2.hint_number, 2)
        self.assertNotEqual(h1.hint_text, h2.hint_text)

        # 3rd unsuccessful submission
        sub3 = Submission.objects.create(
            student=self.student,
            question=self.question,
            code="int main() { char *p = NULL; *p = 1; }",
            status=Submission.Status.RUNTIME_ERROR,
            error_output="Segmentation fault",
        )
        h3 = generate_hint_for_submission(sub3)
        self.assertIsNotNone(h3)
        self.assertEqual(h3.hint_number, 3)

        # 4th unsuccessful submission -> MUST NOT create a 4th hint
        sub4 = Submission.objects.create(
            student=self.student,
            question=self.question,
            code="int main() { return 1; }",
            status=Submission.Status.WRONG_ANSWER,
        )
        h4 = generate_hint_for_submission(sub4)
        total_hints = StudentQuestionHint.objects.filter(student=self.student, question=self.question).count()
        self.assertEqual(total_hints, 3)

        hints_info = get_student_hints_for_question(self.student, self.question)
        self.assertEqual(hints_info["unlocked_count"], 3)
        self.assertFalse(hints_info["can_unlock_more"])

    def test_submission_hints_api(self):
        from .models import Submission, StudentQuestionHint

        sub = Submission.objects.create(
            student=self.student,
            question=self.question,
            code="int main() { return 0; }",
            status=Submission.Status.WRONG_ANSWER,
        )
        StudentQuestionHint.objects.create(
            student=self.student,
            question=self.question,
            submission=sub,
            hint_number=1,
            hint_text="Check boundary constraints.",
            hint_type="diagnostic",
        )

        self.client.force_login(self.student)
        response = self.client.get(reverse("submission_hints_api", args=[sub.id]))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["unlocked_count"], 1)
        self.assertEqual(data["hints"][0]["hint_number"], 1)
        self.assertEqual(data["hints"][0]["hint_text"], "Check boundary constraints.")

    def test_unlock_question_hint_api(self):
        self.client.force_login(self.student)

        # Unlock Hint 1
        res1 = self.client.post(reverse("unlock_question_hint_api", args=[self.question.id]))
        self.assertEqual(res1.status_code, 200)
        d1 = res1.json()
        self.assertTrue(d1["success"])
        self.assertEqual(d1["unlocked_count"], 1)
        self.assertEqual(d1["unlocked_hint"]["hint_number"], 1)
        self.assertTrue(d1["can_unlock_more"])

        # Unlock Hint 2
        res2 = self.client.post(reverse("unlock_question_hint_api", args=[self.question.id]))
        self.assertEqual(res2.status_code, 200)
        d2 = res2.json()
        self.assertEqual(d2["unlocked_count"], 2)
        self.assertEqual(d2["unlocked_hint"]["hint_number"], 2)

        # Unlock Hint 3
        res3 = self.client.post(reverse("unlock_question_hint_api", args=[self.question.id]))
        self.assertEqual(res3.status_code, 200)
        d3 = res3.json()
        self.assertEqual(d3["unlocked_count"], 3)
        self.assertFalse(d3["can_unlock_more"])

        # Attempt 4th unlock -> should return 400
        res4 = self.client.post(reverse("unlock_question_hint_api", args=[self.question.id]))
        self.assertEqual(res4.status_code, 400)
        d4 = res4.json()
        self.assertFalse(d4["success"])

