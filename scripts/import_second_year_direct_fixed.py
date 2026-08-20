import os
import sys
import django
import random
from django.utils.text import slugify

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import User, Question, Module, TestCase

def gen_data_structures():
    """Generate a data structures question"""
    n = random.randint(5, 15)
    # Generate a random array
    arr = [random.randint(1, 100) for _ in range(n)]
    inp = f"{n}\n" + " ".join(map(str, arr)) + "\n"
    # Find maximum element
    ans = str(max(arr))
    desc = """Given an array of integers, find the maximum element.

**Input Format**
First line: integer N (size of array)
Second line: N integers representing the array elements

**Output Format**
Single integer representing the maximum value in the array."""
    return "Maximum Element in Array", desc, inp, ans

def gen_algorithms():
    """Generate an algorithms question"""
    n = random.randint(5, 15)
    # Generate a random array
    arr = [random.randint(1, 100) for _ in range(n)]
    inp = f"{n}\n" + " ".join(map(str, arr)) + "\n"
    # Find if array contains duplicates
    has_dup = len(arr) != len(set(arr))
    ans = "true" if has_dup else "false"
    desc = """Given an array of integers, determine if it contains any duplicates.

**Input Format**
First line: integer N (size of array)
Second line: N integers representing the array elements

**Output Format**
Output 'true' if any value appears at least twice in the array, otherwise output 'false'."""
    return "Contains Duplicates", desc, inp, ans

def gen_object_oriented():
    """Generate an object-oriented programming question"""
    # Simple question about classes
    inp = "Define a class 'Rectangle' with attributes 'width' and 'height', and methods to calculate area and perimeter.\n"
    ans = "class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    \n    def area(self):\n        return self.width * self.height\n    \n    def perimeter(self):\n        return 2 * (self.width + self.height)"
    desc = """Write a Python class 'Rectangle' that represents a rectangle.

**Input Format**
(No input required for this question)

**Output Format**
The complete class definition for Rectangle with:
- Constructor taking width and height parameters
- area() method returning width * height
- perimeter() method returning 2*(width + height)"""
    return "Rectangle Class", desc, inp, ans

def gen_computer_organization():
    """Generate a computer organization question"""
    n = random.randint(8, 16)
    # Generate a random binary number
    binary = ''.join(random.choice('01') for _ in range(n))
    inp = f"{binary}\n"
    # Convert to decimal
    ans = str(int(binary, 2))
    desc = """Given a binary number, convert it to its decimal equivalent.

**Input Format**
A single line containing a binary number (string of 0s and 1s)

**Output Format**
The decimal equivalent of the binary number."""
    return "Binary to Decimal Conversion", desc, inp, ans

def gen_operating_systems():
    """Generate an operating systems question"""
    n = random.randint(1, 20)
    m = random.randint(1, 20)
    inp = f"{n} {m}\n"
    # Simple question: calculate GCD
    import math
    ans = str(math.gcd(n, m))
    desc = """Given two integers, calculate their greatest common divisor (GCD) using the Euclidean algorithm.

**Input Format**
Two integers N and M separated by space

**Output Format**
The GCD of N and M."""
    return "GCD of Two Numbers", desc, inp, ans

# Map module names to generators
GENERATORS_MAP = {
    "Data Structures": gen_data_structures,
    "Algorithms": gen_algorithms,
    "Object-Oriented Programming": gen_object_oriented,
    "Computer Organization": gen_computer_organization,
    "Operating Systems": gen_operating_systems,
}

def create_unique_slug(model_class, title, module):
    """Create a unique slug for the given title and module"""
    base_slug = slugify(title) or "question"
    slug = base_slug
    counter = 1
    while model_class.objects.filter(module=module, slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug

def import_second_year_questions():
    """Import second year programming questions directly with unique slugs."""
    print("Importing second year questions directly...")
    
    # Get or create faculty user
    faculty, _ = User.objects.get_or_create(
        username="faculty_admin",
        defaults={
            "is_staff": True,
            "role": User.Role.FACULTY,
            "email": "faculty@example.com"
        }
    )

    modules_created = 0
    questions_created = 0

    # Process each module
    for i, (module_name, order) in enumerate([
        ("Data Structures", 11),
        ("Algorithms", 12),
        ("Object-Oriented Programming", 13),
        ("Computer Organization", 14),
        ("Operating Systems", 15),
    ], start=0):
        
        generator = GENERATORS_MAP[module_name]
        
        # Get or create module
        module, created = Module.objects.get_or_create(
            name=module_name,
            defaults={
                "order": order,
                "description": f"Second Year {module_name} Module"
            }
        )
        if created:
            modules_created += 1
            print(f"Created module: {module_name}")

        # Import questions for this module
        for q_num in range(5):  # 5 questions per module
            title, desc, inp, ans = generator()
            
            # Create 3 test cases per question
            test_cases = []
            for tc in range(3):
                # Get different test cases by varying the random seed
                random.seed(random.randint(1, 10000) + q_num * 10 + tc)
                _, _, tc_inp, tc_ans = generator()
                test_cases.append({
                    "input": tc_inp,
                    "expected_output": tc_ans,
                    "is_sample": (tc == 0)  # First test case is sample
                })
            
            # Create question with unique slug
            question_title = f"{title} (Module {order})"
            slug = create_unique_slug(Question, question_title, module)
            
            question = Question.objects.create(
                title=question_title,
                slug=slug,
                module=module,
                description=desc,
                starter_code="#include <stdio.h>\n\nint main(void)\n{\n    /* Read from stdin. Do not print prompts unless required. */\n    return 0;\n}",
                language_id=50,  # C (GCC)
                difficulty=["Easy", "Medium", "Hard"][((order - 11) // 2) % 3],  # Distribute difficulties
                is_mandatory=True,
                created_by=faculty
            )
            
            questions_created += 1
            
            # Add test cases
            for tc in test_cases:
                TestCase.objects.create(
                    question=question,
                    stdin=tc["input"],
                    expected_output=tc["expected_output"],
                    is_sample=tc["is_sample"]
                )
            
            print(f"  Created question: {question_title}")

    print(f"Import completed: {modules_created} modules, {questions_created} questions created")

if __name__ == "__main__":
    import_second_year_questions()