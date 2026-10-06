#!/usr/bin/env python
"""
Django management command to seed demo data for E-Lab platform.

This command creates:
- Faculty users
- Student users (first year and second year)
- Sample submissions
- Sample progress data
"""

from django.core.management.base import BaseCommand
from core.models import User, Question, Submission, Progress, Module
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Seeds demo data for E-Lab platform'

    def handle(self, *args, **options):
        self.stdout.write("🚀 Seeding demo data for E-Lab...")
        
        # Create faculty users
        self.stdout.write("\n👨🏫 Creating faculty users...")
        self.create_faculty_users()
        
        # Create student users
        self.stdout.write("\n👩🎓 Creating student users...")
        self.create_student_users()
        
        # Create sample submissions
        self.stdout.write("\n📝 Creating sample submissions...")
        self.create_sample_submissions()
        
        # Create sample progress
        self.stdout.write("\n📊 Creating sample progress data...")
        self.create_sample_progress()
        
        self.stdout.write("\n✅ Demo data seeding completed!")
        self.stdout.write("\n🔑 Test Accounts:")
        self.stdout.write("   HOD: hod / hodpassword")
        self.stdout.write("   Faculty: faculty_cs / faculty123, faculty_it / faculty123")
        self.stdout.write("   Students: student_fy_01 / student123, student_sy_01 / student123 (and others)")
        self.stdout.write("\n📝 Note: First year students see semester 1-2 content, second year see semester 1-4")

    def create_faculty_users(self):
        """Create faculty users with passwords"""
        faculty_data = [
            {
                "username": "faculty_cs",
                "email": "faculty_cs@example.com",
                "full_name": "Computer Science Faculty",
                "password": "faculty123",
                "semester": 1
            },
            {
                "username": "faculty_it",
                "email": "faculty_it@example.com",
                "full_name": "Information Technology Faculty",
                "password": "faculty123",
                "semester": 1
            }
        ]
        
        created = 0
        for data in faculty_data:
            user, created_flag = User.objects.get_or_create(
                username=data["username"],
                defaults={
                    "email": data["email"],
                    "first_name": data["full_name"].split()[0],
                    "last_name": " ".join(data["full_name"].split()[1:]),
                    "role": User.Role.FACULTY,
                    "semester": data["semester"]
                }
            )
            if created_flag:
                user.set_password(data["password"])
                user.save()
                self.stdout.write(self.style.SUCCESS(f'   Created faculty: {user.username} (password: {data["password"]})'))
                created += 1
            else:
                self.stdout.write(f'   Faculty {user.username} already exists')
        
        return created

    def create_student_users(self):
        """Create student users with passwords"""
        first_year_students = [
            {"username": "student_fy_01", "email": "fy01@example.com", "full_name": "First Year Student 1", "base_usn": "1RN21CS001", "semester": 1, "password": "student123"},
            {"username": "student_fy_02", "email": "fy02@example.com", "full_name": "First Year Student 2", "base_usn": "1RN21CS002", "semester": 1, "password": "student123"},
            {"username": "student_fy_03", "email": "fy03@example.com", "full_name": "First Year Student 3", "base_usn": "1RN21CS003", "semester": 2, "password": "student123"},
        ]
        
        second_year_students = [
            {"username": "student_sy_01", "email": "sy01@example.com", "full_name": "Second Year Student 1", "base_usn": "1RN20CS001", "semester": 3, "password": "student123"},
            {"username": "student_sy_02", "email": "sy02@example.com", "full_name": "Second Year Student 2", "base_usn": "1RN20CS002", "semester": 3, "password": "student123"},
            {"username": "student_sy_03", "email": "sy03@example.com", "full_name": "Second Year Student 3", "base_usn": "1RN20CS003", "semester": 4, "password": "student123"},
        ]
        third_year_students = [
            {"username": "student_ty_01", "email": "ty01@example.com", "full_name": "Third Year Student 1", "base_usn": "1RN19CS001", "semester": 5, "password": "student123"},
            {"username": "student_ty_02", "email": "ty02@example.com", "full_name": "Third Year Student 2", "base_usn": "1RN19CS002", "semester": 5, "password": "student123"},
            {"username": "student_ty_03", "email": "ty03@example.com", "full_name": "Third Year Student 3", "base_usn": "1RN19CS003", "semester": 6, "password": "student123"},
        ]

        
        created = 0
        for data in first_year_students + second_year_students + third_year_students:
            # Generate a unique USN based on username to avoid conflicts
            unique_usn = f"{data['base_usn'][:6]}{data['username'][-2:]}"
            
            user, created_flag = User.objects.get_or_create(
                username=data["username"],
                defaults={
                    "email": data["email"],
                    "first_name": data["full_name"].split()[0],
                    "last_name": " ".join(data["full_name"].split()[1:]),
                    "role": User.Role.STUDENT,
                    "semester": data["semester"],
                    "usn": unique_usn
                }
            )
            if created_flag:
                user.set_password(data["password"])
                user.save()
                self.stdout.write(self.style.SUCCESS(f'   Created student: {user.username} (password: {data["password"]}, semester: {data["semester"]}, USN: {unique_usn})'))
                created += 1
            else:
                self.stdout.write(f'   Student {user.username} already exists')
        
        return created

    def create_sample_submissions(self):
        """Create sample submissions for students"""
        students = User.objects.filter(role=User.Role.STUDENT)
        questions = Question.objects.all()
        
        if not students or not questions:
            self.stdout.write(self.style.WARNING("   No students or questions found. Run import_questions first."))
            return 0
        
        status_choices = [
            Submission.Status.ACCEPTED,
            Submission.Status.WRONG_ANSWER,
            Submission.Status.TLE,
            Submission.Status.RUNTIME_ERROR
        ]
        
        sample_codes = {
            "c": """#include <stdio.h>

int main() {
    printf("Hello, World!\\n");
    return 0;
}""",
            "python": """print("Hello, World!")"""
        }
        
        count = 0
        for student in students:
            # Each student gets 3-5 random submissions
            for question in random.sample(list(questions), min(5, len(questions))):
                status = random.choice(status_choices)
                score = random.randint(0, 100) if status == Submission.Status.ACCEPTED else random.randint(0, 50)
                
                submission, created = Submission.objects.get_or_create(
                    student=student,
                    question=question,
                    defaults={
                        "code": sample_codes.get(question.language_id, sample_codes["c"]),
                        "language_id": question.language_id,
                        "status": status,
                        "score": score,
                        "execution_time": random.uniform(0.1, 2.0) if status != Submission.Status.TLE else 5.0,
                        "memory_used": random.randint(1000, 10000),
                        "submitted_at": timezone.now() - timezone.timedelta(days=random.randint(1, 30)),
                        "judged_at": timezone.now()
                    }
                )
                if created:
                    count += 1
        
        self.stdout.write(self.style.SUCCESS(f'   Created {count} sample submissions'))
        return count

    def create_sample_progress(self):
        """Create sample progress data for students"""
        students = User.objects.filter(role=User.Role.STUDENT)
        modules = Module.objects.all()
        
        if not students or not modules:
            self.stdout.write(self.style.WARNING("   No students or modules found."))
            return 0
        
        count = 0
        for student in students:
            # Determine a module level cap based on the student's semester:
            # semester 1-2 → levels 1-2, semester 3-4 → all levels
            max_level = 2 if student.semester <= 2 else 999

            for module in modules:
                # Module has no 'semester' field; use 'level' as a proxy
                if module.level <= max_level:
                    total = random.randint(5, 15)
                    completed = random.randint(0, total)
                    percentage = round((completed / total) * 100) if total else 0

                    progress, created = Progress.objects.get_or_create(
                        student=student,
                        module=module,
                        defaults={
                            "attempted": total,
                            "completed": completed,
                            "percentage": percentage,
                        }
                    )
                    if created:
                        count += 1
        
        self.stdout.write(self.style.SUCCESS(f'   Created {count} sample progress records'))
        return count