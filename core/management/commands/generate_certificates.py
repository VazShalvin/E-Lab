#!/usr/bin/env python
"""
Django management command to generate certificates for eligible students.

A student is eligible if their overall completion percentage across all active
modules meets or exceeds the threshold (default: 80%).
"""

from django.core.management.base import BaseCommand
from django.db.models import Avg

from core.models import Certificate, Progress, User


class Command(BaseCommand):
    help = "Generate certificates for students who have met the completion threshold."

    def add_arguments(self, parser):
        parser.add_argument(
            "--threshold",
            type=float,
            default=80.0,
            help="Minimum average completion percentage required (default: 80).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="List eligible students without creating certificates.",
        )

    def handle(self, *args, **options):
        threshold = options["threshold"]
        dry_run = options["dry_run"]
        semester_label = Certificate.current_semester_label()

        self.stdout.write(
            f"\n🎓 Generating certificates for semester: {semester_label}"
        )
        self.stdout.write(f"   Threshold: {threshold:.0f}%")
        if dry_run:
            self.stdout.write(self.style.WARNING("   DRY RUN — no certificates will be created.\n"))

        students = User.objects.filter(role=User.Role.STUDENT)
        created_count = 0
        skipped_count = 0
        ineligible_count = 0

        for student in students:
            # Compute average completion percentage across all modules
            avg_data = Progress.objects.filter(student=student).aggregate(
                avg_pct=Avg("percentage")
            )
            avg_pct = avg_data["avg_pct"] or 0.0

            if avg_pct < threshold:
                ineligible_count += 1
                self.stdout.write(
                    f"   ✗ {student.username} — {avg_pct:.1f}% (below threshold)"
                )
                continue

            # Check if a certificate already exists for this semester
            existing = Certificate.objects.filter(
                student=student, semester=semester_label
            ).exists()
            if existing:
                skipped_count += 1
                self.stdout.write(
                    f"   ~ {student.username} — already has a certificate for {semester_label}"
                )
                continue

            if dry_run:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"   ✔ {student.username} — eligible ({avg_pct:.1f}%) [DRY RUN]"
                    )
                )
                created_count += 1
                continue

            # Create the certificate
            verification_hash = Certificate.make_hash(student, semester_label, avg_pct)
            cert, cert_created = Certificate.objects.get_or_create(
                student=student,
                semester=semester_label,
                defaults={
                    "completion_percentage": avg_pct,
                    "verification_hash": verification_hash,
                },
            )
            if cert_created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"   ✔ Certificate created for {student.username} ({avg_pct:.1f}%)"
                    )
                )
            else:
                skipped_count += 1

        self.stdout.write(
            f"\n📊 Summary: {created_count} created | {skipped_count} skipped (already existed) | {ineligible_count} ineligible"
        )
