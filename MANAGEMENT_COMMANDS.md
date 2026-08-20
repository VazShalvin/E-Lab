# E-Lab Management Commands

This document describes all available management commands for the E-Lab platform.

## Core Commands

### `create_hod`
**Purpose**: Creates a Head of Department (HOD) user
**Usage**:
```bash
 docker compose exec web python manage.py create_hod
```
**Details**:
- Creates a user with username `hod` and password `hodpassword`
- Sets the user role to HOD
- Grants staff privileges
- **IMPORTANT**: Change the default password immediately after creation

### `import_questions`
**Purpose**: Imports programming questions from CSV files
**Usage**:
```bash
# Import first year questions (default)
docker-compose exec web python manage.py import_questions

# Import second year questions
docker-compose exec web python manage.py import_questions --second-year
```
**Details**:
- Imports questions into the database
- Creates modules as needed
- Assigns questions to appropriate modules
- Sets up test cases for each question

### `generate_certificates`
**Purpose**: Generates certificates for eligible students
**Usage**:
```bash
 docker compose exec web python manage.py generate_certificates
```
**Details**:
- Generates PDF certificates for students with ≥60% completion
- Sends certificates via email if email settings are configured
- Updates certificate status in the database

### `createsuperuser`
**Purpose**: Creates a Django superuser (admin)
**Usage**:
```bash
 docker compose exec web python manage.py createsuperuser
```
**Details**:
- Interactive command to create admin users
- Access the admin interface at `/admin`
- Can manage all aspects of the system

## Database Commands

### `migrate`
**Purpose**: Applies database migrations
**Usage**:
```bash
 docker compose exec web python manage.py migrate
```

### `makemigrations`
**Purpose**: Creates new migrations based on model changes
**Usage**:
```bash
 docker compose exec web python manage.py import_questions
```

### `dumpdata`
**Purpose**: Exports database data
**Usage**:
```bash
# Export all data
docker-compose exec web python manage.py dumpdata > data.json

# Export specific app data
docker-compose exec web python manage.py dumpdata core > core_data.json
```

### `loaddata`
**Purpose**: Imports database data
**Usage**:
```bash
docker-compose exec web python manage.py loaddata data.json
```

## System Commands

### `collectstatic`
**Purpose**: Collects static files for production
**Usage**:
```bash
 docker compose exec web python manage.py collectstatic
```

### `check`
**Purpose**: Checks the system for potential issues
**Usage**:
```bash
docker-compose exec web python manage.py check
```

### `sendtestemail`
**Purpose**: Tests email configuration
**Usage**:
```bash
 docker compose exec web python manage.py sendtestemail your@email.com
```

### `shell`
**Purpose**: Opens a Python shell with Django environment
**Usage**:
```bash
docker-compose exec web python manage.py shell
```

### `dbshell`
**Purpose**: Opens a database shell
**Usage**:
```bash
docker-compose exec web python manage.py dbshell
```

## Custom Commands

### `import_second_year`
**Purpose**: Imports second year programming questions
**Usage**:
```bash
docker-compose exec web python scripts/import_second_year.py
```

### `verify_and_import`
**Purpose**: Imports first year questions from CSV files
**Usage**:
```bash
docker-compose exec web python scripts/verify_and_import.py
```

## Maintenance Commands

### Reset Database (DANGER)
```bash
docker compose down -v  # WARNING: This will delete all data
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py create_hod
docker compose exec web python manage.py import_questions
```

### Backup Database
```bash
docker compose exec postgres pg_dump -U elab_user elab > backup.sql
```

### Restore Database
```bash
docker compose exec -T postgres psql -U elab_user elab < backup.sql
```

## Troubleshooting Commands

### View Logs
```bash
docker compose logs  # All containers
docker compose logs web  # Web container only
docker compose logs postgres  # Database only
```

### Check Container Status
```bash
docker compose ps
```

### Restart Services
```bash
docker compose restart  # Restart all services
docker compose restart web  # Restart web service only
```

### Rebuild Containers
```bash
docker-compose up -d --build
```

## Best Practices

1. **Always backup your database** before running destructive commands
2. **Change default passwords** immediately after creating users
3. **Test email configuration** before generating certificates
4. **Monitor resource usage** when running code execution tasks
5. **Use the setup script** for initial configuration:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

For more information, refer to the [README.md](README.md) file or contact the system administrator.