"""
Seed all courses with proper year/semester availability rules.

Course availability rules:
- C Programming: available from semester 1 (first year, both sems)
- Python: available from semester 3 (second year, odd sem)
- Java: available from semester 3 (second year, odd sem)
- C++: available from semester 5 (third year, odd sem)
- Technical Placement Training: available from semester 3 (second year, both sems)
- Advanced Technical Placement Training: available from semester 5 (third year, both sems)
"""
from django.core.management.base import BaseCommand
from core.models import Course, Module


class Command(BaseCommand):
    help = "Seed course availability rules"

    def handle(self, *args, **options):
        courses_data = [
            {
                "slug": "c-programming",
                "name": "C Programming",
                "description": "Foundational programming course covering variables, control flow, arrays, strings, functions, pointers, and memory management.",
                "available_from_semester": 1,
                "category": "c_programming",
            },
            {
                "slug": "python-programming",
                "name": "Python Programming",
                "description": "Python programming covering data structures, OOP, file handling, and introductory libraries.",
                "available_from_semester": 3,
                "category": "python_programming",
            },
            {
                "slug": "java-programming",
                "name": "Java Programming",
                "description": "Core Java principles, OOP, collections framework, exception handling, and JDBC.",
                "available_from_semester": 3,
                "category": "java_programming",
            },
            {
                "slug": "c-programming-advanced",
                "name": "C++ Programming",
                "description": "Object-oriented programming, classes, inheritance, polymorphism, STL, and templates.",
                "available_from_semester": 5,
                "category": "cpp_programming",
            },
            {
                "slug": "technical-placement-training",
                "name": "Technical Placement Training",
                "description": "Exclusive program for 2nd year CCE students. Master logical building, algorithms, and competitive programming.",
                "available_from_semester": 3,
                "category": "placement_training",
            },
            {
                "slug": "advanced-technical-placement-training",
                "name": "Advanced Technical Placement Training",
                "description": "Exclusive program for 3rd year CCE students. Master advanced algorithms, OOP, Design Patterns, and OS.",
                "available_from_semester": 5,
                "category": "advanced_placement_training",
            },
        ]

        created = 0
        updated = 0
        for data in courses_data:
            course, was_created = Course.objects.update_or_create(
                slug=data["slug"],
                defaults={
                    "name": data["name"],
                    "description": data["description"],
                    "available_from_semester": data["available_from_semester"],
                    "is_active": True,
                },
            )
            if was_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"  Created: {course.name} (available from sem {course.available_from_semester})"))
            else:
                updated += 1
                self.stdout.write(f"  Updated: {course.name} (available from sem {course.available_from_semester})")

        self.stdout.write(f"\nDone! Created: {created}, Updated: {updated}")

        # Verify
        self.stdout.write("\nAll courses:")
        for c in Course.objects.all().order_by("available_from_semester"):
            self.stdout.write(f"  {c.name} — available from semester {c.available_from_semester}")
