#!/usr/bin/env python
"""
Final seed demo script that will work with the actual E-Lab database schema.
Run this with: docker compose exec app python /app/scripts/seed_demo_final.py
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

def create_faculty_users():
    """Create faculty users with passwords"""
    faculty_data = [
        {
            "username": "faculty_cs2",
            "email": "faculty_cs2@example.com",
            "full_name": "Computer Science Faculty 2",
            "password": "faculty123",
            "semester": 1
        },
        {
            "username": "faculty_it2",
            "email": "faculty_it2@example.com",
            "full_name": "Information Technology Faculty 2",
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
            print(f"✅ Created faculty: {user.username} (password: {data['password']})")
        else:
            print(f"ℹ️  Faculty {user.username} already exists")
        created.append(user)
    
    return created

def create_student_users():
    """Create student users with passwords"""
    first_year_students = [
        {"username": "student_fy_11", "email": "fy11@example.com", "full_name": "First Year Student 11", "base_usn": "1RN21CS101", "semester": 1, "password": "student123"},
        {"username": "student_fy_12", "email": "fy12@example.com", "full_name": "First Year Student 12", "base_usn": "1RN21CS102", "semester": 1, "password": "student123"},
        {"username": "student_fy_13", "email": "fy13@example.com", "full_name": "First Year Student 13", "base_usn": "1RN21CS103", "semester": 2, "password": "student123"},
    ]
    
    second_year_students = [
        {"username": "student_sy_11", "email": "sy11@example.com", "full_name": "Second Year Student 11", "base_usn": "1RN20CS101", "semester": 3, "password": "student123"},
        {"username": "student_sy_12", "email": "sy12@example.com", "full_name": "Second Year Student 12", "base_usn": "1RN20CS102", "semester": 3, "password": "student123"},
        {"username": "student_sy_13", "email": "sy13@example.com", "full_name": "Second Year Student 13", "base_usn": "1RN20CS103", "semester": 4, "password": "student123"},
    ]
    
    created = []
    for data in first_year_students + second_year_students:
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
            print(f"✅ Created student: {user.username} (password: {data['password']}, semester: {data['semester']}, USN: {unique_usn})")
        else:
            print(f"ℹ️  Student {user.username} already exists")
        created.append(user)
    
    return created

def create_sample_submissions():
    """Create sample submissions for students"""
    students = User.objects.filter(role=User.Role.STUDENT)
    questions = Question.objects.all()
    
    if not students or not questions:
        print("⚠️  No students or questions found. Run import_questions first.")
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
    
    print(f"✅ Created {count} sample submissions")
    return count

def create_sample_progress():
    """Create sample progress data for students"""
    students = User.objects.filter(role=User.Role.STUDENT)
    modules = Module.objects.all()
    
    if not students or not modules:
        print("⚠️  No students or modules found.")
        return 0
    
    count = 0
    for student in students:
        for module in modules:
            # Get semester from module (handle case where semester field doesn't exist)
            try:
                module_semester = module.semester
            except AttributeError:
                # If semester field doesn't exist, assign based on module name
                module_name = module.name.lower()
                if any(word in module_name for word in ['basics', 'io', 'operators', 'expressions']):
                    module_semester = 1
                elif any(word in module_name for word in ['conditionals', 'loops']):
                    module_semester = 2
                elif any(word in module_name for word in ['arrays', 'strings', 'functions']):
                    module_semester = 3
                else:
                    module_semester = 4
            
            # Only create progress for modules in the student's semester range
            if module_semester <= student.semester:
                # Use the actual fields that exist in the Progress model
                progress, created = Progress.objects.get_or_create(
                    student=student,
                    module=module,
                    defaults={
                        "percentage": random.randint(0, 100),
                    }
                )
                if created:
                    count += 1
    
    print(f"✅ Created {count} sample progress records")
    return count

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
    print("   Faculty: faculty_cs2 / faculty123, faculty_it2 / faculty123")
    print("   Students: student_fy_11 / student123, student_sy_11 / student123 (and others)")
    print("\n📝 Note: First year students see semester 1-2 content, second year see semester 1-4")

if __name__ == "__main__":
    main()