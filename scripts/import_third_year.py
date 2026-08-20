#!/usr/bin/env python
"""
Third Year Import Script
Imports third-year CS/IT questions from JSON files into E-Lab database.
"""
import os
import sys
import json
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import User, Question, Module, TestCase
from django.utils.text import slugify


def import_third_year_questions():
    """Import third year programming questions from JSON file."""
    print("Importing third year questions from JSON...")

    # Get or create faculty user
    faculty, _ = User.objects.get_or_create(
        username="faculty_admin",
        defaults={
            "is_staff": True,
            "role": User.Role.FACULTY,
            "email": "faculty@example.com"
        }
    )

    # Load the generated third year questions JSON
    json_path = "data/third_year_training_questions.json"
    if not os.path.exists(json_path):
        print(f"ERROR: JSON file not found at {json_path}")
        print("Please run generate_third_year_questions.py first")
        return

    with open(json_path, "r") as f:
        data = json.load(f)

    if data.get("category") != "third_year_training":
        print(f"ERROR: Invalid category in JSON: {data.get('category')}")
        return

    modules_created = 0
    questions_created = 0

    # Process each module
    for mod_data in data.get("modules", []):
        module_name = mod_data.get("module")
        module_order = mod_data.get("module_order")
        
        # Get or create module
        module, created = Module.objects.get_or_create(
            name=module_name,
            defaults={
                "order": module_order,
                "description": f"Third Year {module_name} Module"
            }
        )
        if created:
            modules_created += 1
            print(f"Created module: {module_name}")

        # Import questions for this module
        for q_data in mod_data.get("questions", []):
            question, created = Question.objects.get_or_create(
                title=q_data["title"],
                module=module,
                defaults={
                    "description": q_data["description"],
                    "starter_code": q_data.get("starter_code", ""),
                    "language_id": q_data.get("language_id", 50),
                    "difficulty": q_data["difficulty"],
                    "is_mandatory": q_data.get("is_mandatory", True),
                    "created_by": faculty
                }
            )
            
            if created:
                questions_created += 1
                # Generate slug from title
                from django.utils.text import slugify
                base_slug = slugify(q_data["title"]) or "question"
                slug = base_slug
                counter = 1
                while Question.objects.filter(module=module, slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                
                # Update the question with the generated slug
                question.slug = slug
                question.save()
                
                # Add test cases
                for tc in q_data.get("test_cases", []):
                    TestCase.objects.create(
                        question=question,
                        stdin=tc["input"],
                        expected_output=tc["expected_output"],
                        is_sample=tc.get("is_sample", False)
                    )
            else:
                # Question already exists with this title in this module
                # We could update it, but for now we'll skip to avoid duplicates
                pass

    print(f"Import completed: {modules_created} modules, {questions_created} questions created")


if __name__ == "__main__":
    import_third_year_questions()