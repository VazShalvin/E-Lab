# Generated for the CCE e-Lab project.

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("is_superuser", models.BooleanField(default=False, help_text="Designates that this user has all permissions without explicitly assigning them.", verbose_name="superuser status")),
                ("username", models.CharField(error_messages={"unique": "A user with that username already exists."}, help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.", max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name="username")),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="email address")),
                ("is_staff", models.BooleanField(default=False, help_text="Designates whether the user can log into this admin site.", verbose_name="staff status")),
                ("is_active", models.BooleanField(default=True, help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.", verbose_name="active")),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                ("usn", models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ("role", models.CharField(choices=[("student", "Student"), ("faculty", "Faculty"), ("admin", "Admin")], default="student", max_length=16)),
                ("department", models.CharField(blank=True, max_length=80)),
                ("semester", models.PositiveSmallIntegerField(default=1)),
                ("groups", models.ManyToManyField(blank=True, help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.", related_name="user_set", related_query_name="user", to="auth.group", verbose_name="groups")),
                ("user_permissions", models.ManyToManyField(blank=True, help_text="Specific permissions for this user.", related_name="user_set", related_query_name="user", to="auth.permission", verbose_name="user permissions")),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
                ("level", models.PositiveSmallIntegerField(default=1)),
                ("order", models.PositiveSmallIntegerField(default=1)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={"ordering": ["order", "level", "name"]},
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("slug", models.SlugField(max_length=180)),
                ("description", models.TextField()),
                ("difficulty", models.CharField(choices=[("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")], default="easy", max_length=16)),
                ("sample_input", models.TextField(blank=True)),
                ("sample_output", models.TextField(blank=True)),
                ("starter_code", models.TextField(blank=True)),
                ("language_id", models.PositiveIntegerField(default=50, help_text="Language id. 50 is C (GCC).")),
                ("time_limit", models.FloatField(default=2.0)),
                ("memory_limit_kb", models.PositiveIntegerField(default=128000)),
                ("is_mandatory", models.BooleanField(default=True)),
                ("is_active", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("created_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ("module", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="questions", to="core.module")),
            ],
            options={
                "ordering": ["module__order", "title"],
                "unique_together": {("module", "slug")},
            },
        ),
        migrations.CreateModel(
            name="TestCase",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("stdin", models.TextField(blank=True)),
                ("expected_output", models.TextField()),
                ("is_sample", models.BooleanField(default=False)),
                ("order", models.PositiveSmallIntegerField(default=1)),
                ("question", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="test_cases", to="core.question")),
            ],
            options={"ordering": ["order", "id"]},
        ),
        migrations.CreateModel(
            name="Submission",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("code", models.TextField()),
                ("language_id", models.PositiveIntegerField(default=50)),
                ("status", models.CharField(choices=[("pending", "Pending"), ("running", "Running"), ("accepted", "Accepted"), ("wrong_answer", "Wrong Answer"), ("tle", "Time Limit Exceeded"), ("compile_error", "Compilation Error"), ("runtime_error", "Runtime Error"), ("internal_error", "Internal Error")], default="pending", max_length=32)),
                ("score", models.PositiveSmallIntegerField(default=0)),
                ("execution_time", models.FloatField(blank=True, null=True)),
                ("memory_used", models.PositiveIntegerField(blank=True, null=True)),
                ("judge_output", models.TextField(blank=True)),
                ("error_output", models.TextField(blank=True)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("judged_at", models.DateTimeField(blank=True, null=True)),
                ("question", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="submissions", to="core.question")),
                ("student", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="submissions", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-submitted_at"]},
        ),
        migrations.CreateModel(
            name="Progress",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("attempted", models.PositiveIntegerField(default=0)),
                ("completed", models.PositiveIntegerField(default=0)),
                ("percentage", models.FloatField(default=0)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("module", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="progress_rows", to="core.module")),
                ("student", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="progress_rows", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "ordering": ["module__order"],
                "unique_together": {("student", "module")},
            },
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("semester", models.CharField(max_length=32)),
                ("completion_percentage", models.FloatField()),
                ("verification_hash", models.CharField(max_length=96, unique=True)),
                ("pdf", models.FileField(blank=True, upload_to="certificates/pdf/")),
                ("qr_code", models.ImageField(blank=True, upload_to="certificates/qr/")),
                ("issued_at", models.DateTimeField(auto_now_add=True)),
                ("student", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="certificates", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-issued_at"]},
        ),
    ]
