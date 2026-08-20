#!/usr/bin/env python
import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import User
from core.views import import_question_json

def simple_import():
    """Import the canonical Module*.json question banks (docs/QUESTION_JSON_SCHEMA.md)
    without requiring Docker socket access."""
    print("Starting simple import...")

    # Get or create faculty user
    faculty, _ = User.objects.get_or_create(
        username="faculty_admin",
        defaults={
            "is_staff": True,
            "role": User.Role.FACULTY,
            "email": "faculty@example.com"
        }
    )

    # Path to canonical question-bank JSON files
    json_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "generated_level_question_csvs")

    print(f"Looking for JSON files in: {json_dir}")

    if not os.path.exists(json_dir):
        print(f"ERROR: JSON directory not found at {json_dir}")
        print("Please ensure the 'generated_level_question_csvs' directory exists")
        return

    # Import each JSON file (canonical schema; legacy CSV-row JSON also accepted)
    for filename in sorted(os.listdir(json_dir)):
        if not filename.endswith(".json"):
            continue
        filepath = os.path.join(json_dir, filename)
        print(f"Importing {filename}...")
        try:
            with open(filepath, "rb") as f:
                result = import_question_json(f, faculty)
                print(f"Successfully imported {filename}: {result['created']} created, {result['updated']} updated")
        except Exception as e:
            print(f"ERROR importing {filename}: {str(e)}")

    print("Import completed!")

if __name__ == "__main__":
    simple_import()
