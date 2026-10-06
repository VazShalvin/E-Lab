"""
Celery periodic tasks for semester management.
"""
from config.celery import app


@app.task
def auto_advance_semesters_task():
    """Auto-advance student semesters based on current date. Called periodically."""
    from django.utils import timezone
    from datetime import date

    now = timezone.localdate()
    month = now.month

    # Only run on transition dates: Jan 1 and Jul 1
    if month not in (1, 7) or now.day != 1:
        return 0

    from core.models import User

    students = User.objects.filter(role=User.Role.STUDENT)
    updated = 0

    for student in students:
        current_sem = student.semester or 1
        current_year = student.year or 1

        if month == 1:
            # Jan 1: Odd→Even transition (sem +1 if odd)
            if current_sem % 2 == 1:
                new_sem = current_sem + 1
                new_year = current_year
            else:
                continue
        else:
            # Jul 1: Even→Odd transition (sem +1 if even, year +1)
            if current_sem % 2 == 0:
                new_sem = current_sem + 1
                new_year = current_year + 1
            else:
                continue

        # Cap at 4th year
        if new_year > 4:
            new_year = 4
            new_sem = 8 if current_sem >= 6 else new_sem

        User.objects.filter(pk=student.pk).update(
            semester=new_sem,
            year=new_year,
        )
        updated += 1

    return updated
