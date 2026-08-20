# CCE e-Lab - Programming Practice Platform

A self-hosted web platform for Computer & Communication Engineering students to practice programming with automated evaluation, progress tracking, and skill certification.

---

## 🚀 Key Features

- ✅ **Interactive Code Editor** - Practice coding directly in your browser
- ✅ **Automated Evaluation** - Instant feedback on code submissions via isolated sandbox containers
- ✅ **Multi-Language Support** - C (GCC), C++ (G++), Java (OpenJDK), and Python (CPython 3)
- ✅ **Adaptive Question Bank** - Tiered questions with mandatory problem guarantees
- ✅ **Progress Tracking** - Real-time dashboards showing module completion and scores
- ✅ **Skill Certification** - Automated certificate generation and verification hash for qualifying students
- ✅ **Faculty & HOD Portals** - Create modules/questions, review submissions, and manage approvals
- ✅ **Quizzes & Assignments** - Timed quizzes and take-home assignments
- ✅ **LeetCode Integration** - Import public problems directly from LeetCode

---

## 🏗️ Architecture

- **Backend:** Django 5.0 + Django REST Framework
- **Database:** PostgreSQL 15 (`elab-db`)
- **Cache & Message Broker:** Redis 7 (`elab-redis`)
- **Task Runner:** Celery Worker (`elab-worker`)
- **Execution Sandbox:** Custom isolated Docker container (`elab-sandbox`) supporting C, C++, Java, and Python
- **Reverse Proxy:** Nginx (`elab-nginx`)
- **Frontend:** Responsive HTML5 templates + Bootstrap + Ace / Monaco code editor

---

## 📋 Prerequisites

| Software | Minimum Version | Purpose |
|----------|-----------------|---------|
| Docker Engine / Desktop | 24.0+ | Container runtime & execution sandbox |
| Docker Compose | 2.20+ | Multi-container orchestration |
| Git | 2.30+ | Version control |

---

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/VazShalvin/E-Lab.git
cd E-Lab
```

### 2. Configure Environment Variables
Copy the sample environment file:
```bash
cp .env.example .env
```

Ensure the database, redis, and application settings in `.env` match your environment:
```ini
# Django Configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Database Configuration (matches docker-compose.yml)
POSTGRES_DB=elab_db
POSTGRES_USER=elab
POSTGRES_PASSWORD=change-this-password

# Redis & Celery
REDIS_URL=redis://elab-redis:6379/0
CELERY_BROKER_URL=redis://elab-redis:6379/1
CELERY_RESULT_BACKEND=redis://elab-redis:6379/2

# Sandbox Settings
DOCKER_SANDBOX_IMAGE=elab-sandbox
DOCKER_SANDBOX_DIR=/var/elab-sandbox
```

### 3. Build Sandbox & Start Services
```bash
# 1. Build the multi-language execution sandbox image
docker build -t elab-sandbox -f sandbox/Dockerfile sandbox/

# 2. Start all services in the background
docker compose up -d --build
```

### 4. Initialize Database, Static Files & Questions
```bash
# Apply database migrations
docker compose exec app python manage.py migrate

# Collect static files
docker compose exec app python manage.py collectstatic --noinput

# Import default question bank (creates courses and modules)
docker compose exec app python manage.py import_questions

# Seed demo users (HOD, Faculty, First-Year & Second-Year Students)
docker compose exec app python manage.py seed_demo
```

### 5. Access the Application
The web app is available at `http://localhost`:

| URL | Description |
|-----|-------------|
| `http://localhost` | Main Portal / Student Dashboard |
| `http://localhost/login/` | Authentication Page |
| `http://localhost/admin/` | Django Admin Panel |

---

## 🔑 Demo & Test Accounts

Created automatically via `docker compose exec app python manage.py seed_demo`:

| Role | Username | Password | Notes |
|------|----------|----------|-------|
| **HOD** | `hod` | `hodpassword` | Certificate approval, department overview |
| **Faculty (CS)** | `faculty_cs` | `faculty123` | Module & question management |
| **Faculty (IT)** | `faculty_it` | `faculty123` | Module & question management |
| **Student (1st Yr)** | `student_fy_01` | `student123` | Semester 1 student |
| **Student (1st Yr)** | `student_fy_02` | `student123` | Semester 1 student |
| **Student (1st Yr)** | `student_fy_03` | `student123` | Semester 2 student |
| **Student (2nd Yr)** | `student_sy_01` | `student123` | Semester 3 student |
| **Student (2nd Yr)** | `student_sy_02` | `student123` | Semester 3 student |
| **Student (2nd Yr)** | `student_sy_03` | `student123` | Semester 4 student |
| **Student (3rd Yr)** | `student_ty_01` | `student123` | Semester 5 student |
| **Student (3rd Yr)** | `student_ty_02` | `student123` | Semester 6 student |

---
## 🛠️ Management Commands Reference

All commands should be executed against the `app` container:

### Seed Demo Data
Populates faculty, students, sample submissions, and student progress records:
```bash
docker compose exec app python manage.py seed_demo
```

### Import Question Bank CSVs
```bash
# Import first-year questions (default)
docker compose exec app python manage.py import_questions

# Import second-year questions
docker compose exec app python manage.py import_questions --second-year

# Import third-year questions
docker compose exec app python manage.py import_questions --third-year
```

### Generate Student Certificates
Scans student progress and issues certificates to eligible students:
```bash
# Generate certificates (default threshold: 80%)
docker compose exec app python manage.py generate_certificates

# Custom threshold (e.g. 60%)
docker compose exec app python manage.py generate_certificates --threshold 60

# Dry-run mode (preview eligible students without writing records)
docker compose exec app python manage.py generate_certificates --dry-run
```

### Import Questions from LeetCode
```bash
# Import by slug
docker compose exec app python manage.py import_leetcode --question two-sum --module "LeetCode Problems" --difficulty easy --csv-level 1

# Import by ID
docker compose exec app python manage.py import_leetcode --question 1 --module "LeetCode Problems" --difficulty easy
```

### Create Head of Department (HOD) / Superuser
```bash
# Create dedicated HOD user
docker compose exec app python manage.py create_hod

# Create Django Superuser
docker compose exec app python manage.py createsuperuser
```

---

## 📦 Docker Sandbox Execution

The custom Docker sandbox executes code submissions without external dependencies:

| Language | `language_id` | Toolchain | Strictness / Options |
|----------|---------------|-----------|----------------------|
| **C** | 50 | GCC (`gcc -std=c11`) | `-Wall -Wextra` |
| **C++** | 54 | GCC (`g++ -std=c++17`) | `-Wall -Wextra` |
| **Java** | 62 | OpenJDK 17 (`javac`/`java`) | Auto-detects public class |
| **Python** | 71 | CPython 3 (`python3`) | Syntax check & isolated execution |

### Sandbox Security Flags:
- **No Network:** Submissions run with `--network none`
- **Dropped Capabilities:** `--cap-drop ALL`
- **Resource Limits:** Restricted memory, CPU time, and PID limits
- **Ephemeral:** Fresh containers spawned per submission and cleaned up automatically

---

## 🔧 Useful Docker & Maintenance Commands

```bash
# View live logs
docker compose logs -f app
docker compose logs -f worker
docker compose logs -f elab-db

# Restart services after configuration change
docker compose restart app worker nginx

# Run test suite
docker compose exec app python manage.py test

# Backup database
docker compose exec elab-db pg_dump -U elab elab_db > backup.sql

# Restore database
docker compose exec -T elab-db psql -U elab elab_db < backup.sql
```

---

## 🔍 Troubleshooting

### 1. `DisallowedHost` or `Bad Request (400)`
- Ensure `ALLOWED_HOSTS` in `.env` includes `localhost,127.0.0.1` and your server's domain/IP.
- Restart app: `docker compose restart app`.

### 2. Database Connection Error
- Ensure container `elab-db` is running: `docker compose ps`.
- Check database logs: `docker compose logs elab-db`.
- Verify database credentials in `.env` match `POSTGRES_DB`, `POSTGRES_USER`, and `POSTGRES_PASSWORD`.

### 3. Static Files Not Loading / Unstyled UI
- Run static collection:
  ```bash
  docker compose exec app python manage.py collectstatic --noinput
  docker compose restart nginx
  ```

### 4. Sandbox Execution Errors
- Make sure the sandbox image is built locally:
  ```bash
  docker build -t elab-sandbox -f sandbox/Dockerfile sandbox/
  ```
- Ensure Docker socket is accessible if required or sandbox directory permissions are correct.

---

## 📄 License
Academic use — Department of Computer & Communication Engineering (CCE), NMAM Institute of Technology, Nitte.

### Ingest Questions into RAG Database
Builds vector embeddings for the AI question generator:
```bash
# Run once to ingest all DSA topics into ChromaDB
docker compose exec app python manage.py rag_ingest
```
