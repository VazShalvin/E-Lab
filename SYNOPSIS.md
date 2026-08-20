# CCE e-Lab Project Synopsis

## Overview

CCE e-Lab is a self-hosted programming lab platform designed to run on a college server and serve students through lab PCs on the LAN. Students solve programming questions in the browser, submit code, receive automatic evaluation results, track module-wise progress, and generate a verifiable completion certificate when eligible.

The system is packaged for deployment with Docker Compose, so the lab server can clone the GitHub repository, configure environment variables, and start all required services together.

## Main Users

- **Students** sign up, view modules, solve questions, submit C code, track progress, and download certificates.
- **Faculty** create modules, questions, and test cases, and monitor recent submissions.
- **Admins** use Django admin for complete data management, user management, and system oversight.

## Technology Stack

- **Django**: Main web application and backend.
- **Django REST Framework**: API endpoints for submissions, questions, and progress.
- **PostgreSQL**: Main application database.
- **Redis**: Queue backend for background code evaluation.
- **Celery**: Background worker that processes submitted code for execution in the custom Docker sandbox.
- **Nginx**: Reverse proxy that exposes the app on port 80 and serves static/media files.
- **Docker Compose**: Runs the full stack on the lab server.

## How The System Works

### 1. Student Login And Dashboard

Students log in through the web interface. The dashboard shows active modules, completion percentage, module progress, and certificate availability.

Important files:

- `core/views.py`: Dashboard and student page logic.
- `templates/student/dashboard.html`: Student dashboard UI.
- `core/services.py`: Progress calculation.

### 2. Modules And Questions

Faculty create modules such as "Basics and I/O" or "Control Flow". Each module contains programming questions. A question has a title, description, sample input/output, starter code, language ID, time limit, memory limit, and mandatory status.

Important files:

- `core/models.py`: `Module`, `Question`, and `TestCase` models.
- `templates/faculty/question_form.html`: Faculty question form.
- `core/admin.py`: Django admin setup.

### 3. Test Cases

Each question can have sample and hidden test cases. Sample tests are visible to students, while hidden tests are used for judging correctness.

Important model:

- `TestCase`

Fields include:

- `stdin`
- `expected_output`
- `is_sample`
- `order`

### 4. Code Submission Flow

When a student submits code:

1. The app saves the submission in the database with `pending` status.
2. A Celery task is queued.
3. The worker sends the code and test input to the custom Docker sandbox.
4. The sandbox compiles and runs the code.
5. The worker reads the sandbox result.
6. The submission status, score, time, memory, and output are saved.
7. Student progress is recalculated.

Important files:

- `core/views.py`: Creates submissions.
- `core/tasks.py`: Celery task entry point.
- `core/services.py`: Custom sandbox communication and evaluation logic.
- `templates/student/submission_detail.html`: Result page.


### 6. Progress Tracking

Progress is calculated from accepted submissions. For each module, the system counts:

- Total active questions
- Attempted questions
- Accepted questions
- Completion percentage

Important model:

- `Progress`

Important functions:

- `update_progress`
- `student_progress`
- `overall_percentage`

These are in `core/services.py`.

### 7. Certificate Generation

When a student completes the required percentage and all mandatory questions, the system can generate a certificate.

Certificate features:

- PDF file generation
- QR code generation
- Verification hash
- Public verification page

Important files:

- `core/models.py`: `Certificate` model.
- `core/services.py`: `generate_certificate`.
- `templates/certificates/certificate.html`: PDF certificate template.
- `templates/certificates/verify.html`: Verification page.

Certificate eligibility is controlled by:

```text
CERTIFICATE_THRESHOLD=60
```

in `.env`.

### 8. Faculty Dashboard

Faculty can view:

- Number of students
- Number of questions
- Modules
- Recent submissions

Faculty can also create:

- Modules
- Questions
- Test cases

Important files:

- `templates/faculty/dashboard.html`
- `templates/faculty/form.html`
- `templates/faculty/question_form.html`
- `core/views.py`

### 9. Admin Panel

Django admin is available at:

```text
/admin/
```

Admins can manage:

- Users
- Modules
- Questions
- Test cases
- Submissions
- Progress
- Certificates

Important file:

- `core/admin.py`

## Deployment Architecture

On the lab server, Docker Compose starts these services:

- `app`: Django + Gunicorn web app
- `worker`: Celery worker
- `nginx`: Public reverse proxy on port 80
- `elab-db`: PostgreSQL database for the app
- `elab-redis`: Redis queue for Celery


Users access only:

```text
http://SERVER_IP/
```

Nginx forwards requests internally to Django.

## Important Project Files

- `README.md`: Deployment commands and quick start.
- `SYNOPSIS.md`: This project explanation.
- `.env.example`: Environment variable template.
- `docker-compose.yml`: Full service stack.
- `Dockerfile`: Django app container image.
- `deploy/nginx.conf`: Nginx reverse proxy config.
- `requirements.txt`: Python dependencies.
- `manage.py`: Django command runner.
- `config/settings.py`: Django settings.
- `config/urls.py`: Root URL configuration.
- `core/models.py`: Database models.
- `core/views.py`: Web page and API logic.
- `core/services.py`: Business logic, custom sandbox, progress, certificates.
- `core/tasks.py`: Celery background jobs.
- `core/forms.py`: Django forms.
- `core/serializers.py`: API serializers.
- `core/management/commands/seed_demo.py`: Demo data command.
- `templates/`: HTML pages.
- `static/css/app.css`: Main styling.

## Server Setup Summary

On the Ubuntu lab server:

```bash
git clone <your-github-repo-url> /opt/elab
cd /opt/elab
cp .env.example .env
nano .env
docker compose up -d --build
docker compose exec app python manage.py migrate
docker compose exec app python manage.py collectstatic --noinput
docker compose exec app python manage.py seed_demo
docker compose exec app python manage.py createsuperuser
```

Then open:

```text
http://SERVER_IP/
```

## Current Status

The project is currently an MVP implementation. The main software pieces are present and local Django checks passed. The remaining work is full Docker testing on the actual Ubuntu server, adding real college questions, updating branding, and validating custom sandbox execution under real lab load.
