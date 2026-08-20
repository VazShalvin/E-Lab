#!/usr/bin/env python
import os
import sys
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import User, Question, Module, TestCase
from django.core.files import File

def import_second_year_questions():
    """Import second year programming questions for advanced modules."""
    print("Importing second year questions...")
    
    # Get or create faculty user
    faculty, _ = User.objects.get_or_create(
        username="faculty_admin", 
        defaults={
            "is_staff": True, 
            "role": User.Role.FACULTY, 
            "email": "faculty@example.com"
        }
    )
    
    # Create second year modules if they don't exist
    module_names = [
        "Data Structures",
        "Algorithms",
        "Object-Oriented Programming",
        "Computer Organization",
        "Operating Systems"
    ]
    
    modules = []
    for i, name in enumerate(module_names, start=11):  # Start numbering after existing modules
        module, created = Module.objects.get_or_create(
            name=name,
            defaults={
                "order": i,
                "description": f"Second Year {name} Module"
            }
        )
        modules.append(module)
        if created:
            print(f"Created module: {name}")
    
    # Sample questions for second year
    questions = [
        {
            "module": modules[0],  # Data Structures
            "title": "Binary Tree Implementation",
            "description": "Implement a binary tree with insert, search, and delete operations.",
            "starter_code": "#include <stdio.h>\n#include <stdlib.h>\n\nstruct Node {\n    int data;\n    struct Node* left;\n    struct Node* right;\n};\n\nstruct Node* createNode(int data) {\n    // Your implementation here\n}",
            "language_id": 50,  # C
            "difficulty": Question.Difficulty.MEDIUM,
            "is_mandatory": True,
            "test_cases": [
                {"stdin": "5", "expected_output": "5 inserted"},
                {"stdin": "3", "expected_output": "3 inserted"},
            ]
        },
        {
            "module": modules[1],  # Algorithms
            "title": "Dijkstra's Algorithm",
            "description": "Implement Dijkstra's shortest path algorithm.",
            "starter_code": "#include <stdio.h>\n#include <limits.h>\n\n#define V 9\n\nint minDistance(int dist[], bool sptSet[]) {\n    // Your implementation here\n}\n\nvoid dijkstra(int graph[V][V], int src) {\n    // Your implementation here\n}",
            "language_id": 50,
            "difficulty": Question.Difficulty.HARD,
            "is_mandatory": True,
            "test_cases": [
                {"stdin": "0", "expected_output": "Vertex\tDistance from Source"},
            ]
        },
        # Add more questions as needed
    ]
    
    # Import questions
    for q in questions:
        question, created = Question.objects.get_or_create(
            title=q["title"],
            module=q["module"],
            defaults={
                "description": q["description"],
                "starter_code": q["starter_code"],
                "language_id": q["language_id"],
                "difficulty": q["difficulty"],
                "is_mandatory": q["is_mandatory"],
                "created_by": faculty
            }
        )
        
        if created:
            print(f"Created question: {q['title']}")
            # Add test cases
            for tc in q["test_cases"]:
                TestCase.objects.create(
                    question=question,
                    stdin=tc["stdin"],
                    expected_output=tc["expected_output"],
                    is_sample=True
                )
        else:
            print(f"Question already exists: {q['title']}")
    
    print("Second year questions import completed!")

if __name__ == "__main__":
    import_second_year_questions()