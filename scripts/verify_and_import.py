import os
import sys

import django

from core.models import User, Question
from core.services import choose_adaptive_questions
from core.views import import_question_json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# Get or create faculty user for import
faculty, _ = User.objects.get_or_create(username="admin_gen", defaults={"is_staff": True, "role": User.Role.FACULTY, "email": "admin@example.com"})

# Get or create dummy student for testing
student, _ = User.objects.get_or_create(username="student_test", defaults={"role": User.Role.STUDENT, "email": "student@example.com", "usn": "1RN21CS999"})

# Path to JSON files
JSON_DIR = os.path.join(PROJECT_ROOT, "generated_level_question_csvs")

json_files = [
    "Module1_Basics_IO_Levels.json",
    "Module2_Operators_Expressions_Levels.json",
    "Module3_Conditionals_Loops_Levels.json",
    "Module4_Arrays_Levels.json",
    "Module5_Strings_Levels.json",
    "Module6_Functions_Levels.json",
    "Module7_Pointers_Levels.json",
    "Module8_Structures_Levels.json",
    "Module9_File_Handling_Levels.json",
    "Module10_Advanced_Concepts_Levels.json"
]

def main():
    print("Starting JSON import...")
    print(f"Looking for JSON files in: {JSON_DIR}")

    # Check if directory exists
    if not os.path.exists(JSON_DIR):
        print(f"ERROR: JSON directory not found at {JSON_DIR}")
        print("Please ensure the 'generated_level_question_csvs' directory exists in your project root")
        sys.exit(1)

    # Get or create faculty user for import
    faculty, _ = User.objects.get_or_create(
        username="faculty_admin", 
        defaults={
            "is_staff": True, 
            "role": User.Role.FACULTY, 
            "email": "faculty@example.com"
        }
    )
    
    # Initialize imported modules list
    imported_modules = []
    
    for filename in json_files:
        filepath = os.path.join(JSON_DIR, filename)
        
        if not os.path.exists(filepath):
            print(f"WARNING: File not found: {filepath}")
            continue
            
        try:
            with open(filepath, "rb") as f:
                res = import_question_json(f, faculty)
            modules = res.get("modules") or ([res["module"]] if res["module"] else [])
            imported_modules.extend(modules)
            for module in modules:
                total = module.questions.count()
                mand = module.questions.filter(is_mandatory=True).count()
                print(f"[{module.name} (Order {module.order})] Created: {res['created']} | Updated: {res['updated']} | Total Qs: {total} | Mandatory Qs: {mand}")
        except Exception as e:
            print(f"ERROR importing {filename}: {str(e)}")
            continue

    # Testing Adaptive Selection & Mandatory Guarantee
    print("\nTesting Adaptive Selection & Mandatory Guarantee...")
    try:
        # Get or create a test student for the adaptive selection test
        test_student, _ = User.objects.get_or_create(
            username="student_test",
            defaults={"role": User.Role.STUDENT, "email": "student_test@example.com", "usn": "1RN21CS999"}
        )
        for module in imported_modules:
            # Correct call: choose_adaptive_questions(student, module, difficulty, count)
            questions = choose_adaptive_questions(test_student, module, Question.Difficulty.EASY, count=5)
            mandatory_questions = [q for q in questions if q.is_mandatory]
            print(f"Module: {module.name} - Selected {len(questions)} questions, {len(mandatory_questions)} mandatory")
    except Exception as e:
        print(f"Error during adaptive selection test: {str(e)}")

    print("\nQuestions import completed!")
    for module in imported_modules:  # test all modules
        # Test Easy randomization
        easy_1 = choose_adaptive_questions(student, module, Question.Difficulty.EASY, count=5)
        easy_2 = choose_adaptive_questions(student, module, Question.Difficulty.EASY, count=5)
        e_ids_1 = sorted([q.slug for q in easy_1])
        e_ids_2 = sorted([q.slug for q in easy_2])
        print(f"\n{module.name} - Easy Pick 1 count: {len(e_ids_1)}")
        print(f"{module.name} - Easy Pick 2 count: {len(e_ids_2)}")
        
        # Test Hard Mandatory Guarantee
        hard_qs = choose_adaptive_questions(student, module, Question.Difficulty.HARD, count=5)
        hard_slugs = [q.slug for q in hard_qs]
        mand_slugs = [q.slug for q in module.questions.filter(difficulty=Question.Difficulty.HARD, is_mandatory=True)]
        
        all_mand_included = all(s in hard_slugs for s in mand_slugs)
        print(f"{module.name} - Hard Pick count: {len(hard_slugs)} | Mandatory count required: {len(mand_slugs)} | All Mandatory Included: {all_mand_included}")

print("\nVerification Complete!")