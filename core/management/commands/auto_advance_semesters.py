#!/usr/bin/env python
"""
Django management command to auto-advance student semesters.

Rules:
- Jan 1: Odd→Even transition (semester +1 if odd), year stays same
- Jul 1: Even→Odd transition (semester +1 if even), year stays same
- When semester goes from 2→3, 4→5, or 6→7: year increases by 1
- Students cap at year 4 (semester 7-8)
"""
import logging
from datetime import date

from django.core.management.base import BaseCommand
from django.utils import timezone

from core.models import User

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Auto-advance student semesters based on current date"

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Show what would change without making changes",
        )

    def handle(self, *args, **options):
        dry_run = options["dry_run"]
        now = timezone.localdate()
        month = now.month

        # Only run on transition dates: Jan 1 and Jul 1
        if month not in (1, 7) or now.day != 1:
            self.stdout.write(
                f"No semester transition today ({now}). "
                f"Next transitions: Jan 1 (odd→even) and Jul 1 (even→odd)."
            )
            return

        year = now.year
        if month == 1:
            transition_type = "odd_to_even"
            label = f"{year}-{str(year + 1)[-2:]} Even"
        else:
            transition_type = "even_to_odd"
            label = f"{year}-{str(year + 1)[-2:]} Odd"

        self.stdout.write(
            f"🔄 Semester transition: {transition_type} | "
            f"Academic year: {label}"
        )

        students = User.objects.filter(role=User.Role.STUDENT)
        updated = 0
        already_current = 0

        for student in students:
            current_sem = student.semester or 1
            current_year = student.year or 1

            if transition_type == "odd_to_even":
                # Odd sem (1,3,5,7) → even sem (2,4,6,8)
                if current_sem % 2 == 1:  # odd
                    new_sem = current_sem + 1
                    new_year = current_year
                else:
                    already_current = 1
                    continue
            else:  # even_to_odd
                # Even sem (2,4,6,8) → odd sem (3,5,7) + year +1
                if current_sem % 2 == 0:  # even
                    new_sem = current_sem + 1
                    new_year = current_year + 1
                else:
                    already_current = 1
                    continue

            # Cap at 4th year (semester 7-8)
            if new_year > 4:
                new_year = 4
                new_sem = 8 if current_sem >= 6 else new_sem

            if dry_run:
                self.stdout.write(
                    f"  Would update: {student.username} (ID:{student.pk}) "
                    f"Sem {current_sem}→{new_sem}, Year {current_year}→{new_year}"
                )
            else:
                User.objects.filter(pk=student.pk).update(
                    semester=new_sem,
                    year=new_year,
                )
                self.stdout.write(
                    f"  Updated: {student.username} (ID:{student.pk}) "
                    f"Sem {current_sem}→{new_sem}, Year {current_year}→{new_year}"
                )
                updated += 1

        self.stdout.write(
            f"\nSummary: {updated} students advanced | {already_current} already at current semester"
        )
        if dry_run:
            self.stdout.write(self.style.WARNING("DRY RUN — no changes saved"))
