#!/usr/bin/env python
"""
Seed demo data for E-Lab platform.

This script creates:
- Faculty users
- Student users (first year and second year)
- Sample submissions
- Sample progress data
"""

import os
import sys
import random

import django

# Set up Django
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import User, Question, Submission, Progress, Module
from django.utils import timezone

# Sample data
def create_faculty_users():
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
    
    created = []
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
            print(f"Created faculty: {user.username} (password: {data['password']})")
        else:
            print(f"Faculty {user.username} already exists")
        created.append(user)
    
    return created

def create_student_users():
    """Create student users with passwords"""
    first_year_students = [
        {"username": "student_fy_01", "email": "fy01@example.com", "full_name": "First Year Student 1", "usn": "1RN21CS001", "semester": 1, "password": "student123"},
        {"username": "student_fy_02", "email": "fy02@example.com", "full_name": "First Year Student 2", "usn": "1RN21CS002", "semester": 1, "password": "student123"},
        {"username": "student_fy_03", "email": "fy03@example.com", "full_name": "First Year Student 3", "usn": "1RN21CS003", "semester": 2, "password": "student123"},
    ]
    
    second_year_students = [
        {"username": "student_sy_01", "email": "sy01@example.com", "full_name": "Second Year Student 1", "usn": "1RN20CS001", "semester": 3, "password": "student123"},
        {"username": "student_sy_02", "email": "sy02@example.com", "full_name": "Second Year Student 2", "usn": "1RN20CS002", "semester": 3, "password": "student123"},
        {"username": "student_sy_03", "email": "sy03@example.com", "full_name": "Second Year Student 3", "usn": "1RN20CS003", "semester": 4, "password": "student123"},
    ]
    
    created = []
    for data in first_year_students + second_year_students:
        user, created_flag = User.objects.get_or_create(
            username=data["username"],
            defaults={
                "email": data["email"],
                "first_name": data["full_name"].split()[0],
                "last_name": " ".join(data["full_name"].split()[1:]),
                "role": User.Role.STUDENT,
                "semester": data["semester"],
                "usn": data["usn"]
            }
        )
        if created_flag:
            user.set_password(data["password"])
            user.save()
            print(f"Created student: {user.username} (password: {data['password']}, semester: {data['semester']})")
        else:
            print(f"Student {user.username} already exists")
        created.append(user)
    
    return created

def create_sample_submissions():
    """Create sample submissions for students"""
    students = User.objects.filter(role=User.Role.STUDENT)
    questions = Question.objects.all()
    
    if not students or not questions:
        print("No students or questions found. Run import_questions first.")
        return
    
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
    
    print(f"Created {count} sample submissions")

def create_sample_progress():
    """Create sample progress data for students"""
    students = User.objects.filter(role=User.Role.STUDENT)
    modules = Module.objects.all()
    
    if not students or not modules:
        print("No students or modules found.")
        return
    
    count = 0
    for student in students:
        for module in modules:
            # Only create progress for modules in the student's semester range
            if module.semester <= student.semester:
                progress, created = Progress.objects.get_or_create(
                    student=student,
                    module=module,
                    defaults={
                        "completed_questions": random.randint(0, 10),
                        "total_questions": random.randint(5, 15),
                        "percentage": random.randint(0, 100),
                        "last_attempted": timezone.now() - timezone.timedelta(days=random.randint(1, 30))
                    }
                )
                if created:
                    count += 1
    
    print(f"Created {count} sample progress records")

def main():
    print("🚀 Seeding demo data for E-Lab...")
    
    # Create faculty users
    print("\n👨🏫 Creating faculty users...")
    create_faculty_users()
    
    # Create student users
    print("\n👩🎓 Creating student users...")
    create_student_users()
    
    # Create sample submissions
    print("\n📝 Creating sample submissions...")
    create_sample_submissions()
    
    # Create sample progress
    print("\n📊 Creating sample progress data...")
    create_sample_progress()
    
    print("\n✅ Demo data seeding completed!")
    print("\n🔑 Test Accounts:")
    print("   HOD: hod / hodpassword")
    print("   Faculty: faculty_cs / faculty123, faculty_it / faculty123")
    print("   Students: student_fy_01 / student123, student_sy_01 / student123 (and others)")
    print("\n📝 Note: First year students see semester 1-2 content, second year see semester 1-4")

if __name__ == "__main__":
    main()