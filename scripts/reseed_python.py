import os
import sys

sys.path.append('/app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from core.models import Course, Module, Question, TestCase
from django.utils.text import slugify

def seed_python():
    course = Course.objects.get(slug='python-programming')
    
    print("Deleting existing Python modules and questions...")
    Module.objects.filter(course=course).delete()
    
    print("Creating 15 modules...")
    modules = []
    for i in range(1, 16):
        m = Module.objects.create(
            name=f"Module {i}", 
            course=course, 
            category="python_programming", 
            order=i, 
            level=i
        )
        modules.append(m)
        
    print("Adding 15 Mandatory Lab Manual Questions...")
    
    # We will pick 15 distinct questions from the provided images (excluding plotting)
    # Q1: Palindrome Check (Module 1)
    q1 = Question.objects.create(
        module=modules[0],
        title="Palindrome Check",
        slug="python-palindrome-check",
        description="Write a Python program to check whether a given string is a palindrome or not.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q1, is_sample=True, order=1, stdin="radar", expected_output="True")
    TestCase.objects.create(question=q1, is_sample=False, order=2, stdin="hello", expected_output="False")

    # Q2: Prime Numbers in Interval (Module 2)
    q2 = Question.objects.create(
        module=modules[1],
        title="Prime Numbers in Interval",
        slug="python-prime-interval",
        description="Write a Python program to print all prime numbers in an interval (start and end included). Input two numbers separated by a newline.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q2, is_sample=True, order=1, stdin="10\n20", expected_output="11\n13\n17\n19")
    
    # Q3: Pangram Check (Module 3)
    q3 = Question.objects.create(
        module=modules[2],
        title="Pangram Check",
        slug="python-pangram",
        description="Write a Python program to check if a given sentence is a pangram (contains all 26 letters of the English alphabet) or not. Output 'True' or 'False'.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q3, is_sample=True, order=1, stdin="The quick brown fox jumps over the lazy dog", expected_output="True")
    TestCase.objects.create(question=q3, is_sample=False, order=2, stdin="Hello world", expected_output="False")

    # Q4: Sum of Digits (Module 4)
    q4 = Question.objects.create(
        module=modules[3],
        title="Sum of Digits",
        slug="python-sum-digits",
        description="Write a Python program to find the sum of digits of the given number.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q4, is_sample=True, order=1, stdin="1234", expected_output="10")
    
    # Q5: Armstrong Number (Module 5)
    q5 = Question.objects.create(
        module=modules[4],
        title="Armstrong Number Check",
        slug="python-armstrong",
        description="Write a Python program to check if a 3-digit number is an Armstrong number or not. Output 'True' or 'False'.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q5, is_sample=True, order=1, stdin="153", expected_output="True")
    TestCase.objects.create(question=q5, is_sample=False, order=2, stdin="100", expected_output="False")
    
    # Q6: Fibonacci Series (Module 6)
    q6 = Question.objects.create(
        module=modules[5],
        title="Fibonacci Series",
        slug="python-fibonacci",
        description="Write a Python program to generate the Fibonacci series up to N terms. Print the terms space-separated.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q6, is_sample=True, order=1, stdin="5", expected_output="0 1 1 2 3")
    
    # Q7: Rock, Paper, Scissors (Module 7)
    q7 = Question.objects.create(
        module=modules[6],
        title="Rock, Paper, Scissors",
        slug="python-rps",
        description="Write a Python program to implement Rock, Paper, Scissor game. Read Player 1's choice and Player 2's choice on separate lines. Display the winner ('Player 1', 'Player 2', or 'Tie').",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q7, is_sample=True, order=1, stdin="Rock\nScissors", expected_output="Player 1")
    TestCase.objects.create(question=q7, is_sample=False, order=2, stdin="Paper\nPaper", expected_output="Tie")

    # Q8: Factorial using Recursion (Module 8)
    q8 = Question.objects.create(
        module=modules[7],
        title="Factorial using Recursion",
        slug="python-factorial-recursion",
        description="Write a Python program to find the factorial of a number using recursion.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q8, is_sample=True, order=1, stdin="5", expected_output="120")
    
    # Q9: Bubble Sort (Module 9)
    q9 = Question.objects.create(
        module=modules[8],
        title="Bubble Sort",
        slug="python-bubble-sort",
        description="Write a Python program to perform bubble sort on a given set of space-separated numbers.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q9, is_sample=True, order=1, stdin="5 2 9 1 5 6", expected_output="1 2 5 5 6 9")
    
    # Q10: String Manipulation - First/Last Chars (Module 10)
    q10 = Question.objects.create(
        module=modules[9],
        title="String from Ends",
        slug="python-string-ends",
        description="Write a Python program to make a string from the first two and last two characters from a given string. If the string length is less than 2, return 'Empty String'.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q10, is_sample=True, order=1, stdin="python", expected_output="pyon")
    TestCase.objects.create(question=q10, is_sample=False, order=2, stdin="w", expected_output="Empty String")

    # Q11: Binary Search (Module 11)
    q11 = Question.objects.create(
        module=modules[10],
        title="Binary Search",
        slug="python-binary-search",
        description="Write a Python program to perform binary search on a sorted list of space-separated integers. The first line is the list, the second line is the target. Print the index if found, else -1.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q11, is_sample=True, order=1, stdin="1 3 5 7 9\n5", expected_output="2")
    TestCase.objects.create(question=q11, is_sample=False, order=2, stdin="1 3 5\n10", expected_output="-1")
    
    # Q12: Traffic Light (Module 12)
    q12 = Question.objects.create(
        module=modules[11],
        title="Traffic Light Simulator",
        slug="python-traffic-light",
        description="""Write a program that simulates a traffic light. 
1. Function `trafficLight()` accepts input.
2. Function `light()` accepts string (RED, YELLOW, GREEN) and returns 0, 1, or 2.
3. Based on return:
   0 -> 'STOP, your life is precious'
   1 -> 'Please WAIT, till the light is Green'
   2 -> 'GO! Thank you for being patient'
Invalid input prints error. At the end, print 'SPEED THRILLS BUT KILLS'.""",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q12, is_sample=True, order=1, stdin="RED", expected_output="STOP, your life is precious\nSPEED THRILLS BUT KILLS")
    
    # Q13: Student Grades (Module 13)
    q13 = Question.objects.create(
        module=modules[12],
        title="Student Grades",
        slug="python-student-grades",
        description="Given an integer N, followed by N lines of student info (Format: `Name Sub1 Sub2 Sub3`). Calculate the average for each student and print `Name: Average`. Finally print the class average as `Class Average: Value` (round to 2 decimals).",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q13, is_sample=True, order=1, stdin="2\nAlice 90 80 100\nBob 70 60 80", expected_output="Alice: 90.00\nBob: 70.00\nClass Average: 80.00")
    
    # Q14: String Operations (Module 14)
    q14 = Question.objects.create(
        module=modules[13],
        title="Multiple String Operations",
        slug="python-string-ops",
        description="Take string input. Print each on a new line:\na) length\nb) uppercase\nc) contains 'python' (True/False)\nd) space-separated words (as string list representation)\ne) joined with hyphen '-'\nf) reversed",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q14, is_sample=True, order=1, stdin="I love python", expected_output="13\nI LOVE PYTHON\nTrue\n['I', 'love', 'python']\nI-love-python\nnohtyp evol I")

    # Q15: CSV File Operations - Top Scorer (Module 15)
    q15 = Question.objects.create(
        module=modules[14],
        title="CSV Top Scorer",
        slug="python-csv-top-scorer",
        description="Given N students (USN, Name, Phone, Marks) space-separated. Write them to a CSV, read it, sort by USN, and then display the Name of the top scorer.",
        difficulty="hard",
        csv_level=3,
        language_id=71,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q15, is_sample=True, order=1, stdin="3\n1 Bob 123 85\n3 Alice 456 95\n2 Charlie 789 90", expected_output="Alice")

    print("Added all 15 mandatory questions.")

if __name__ == '__main__':
    seed_python()
