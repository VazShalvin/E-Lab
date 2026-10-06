import os
import sys

from core.models import Course, Module, Question, TestCase
from django.core.management import call_command
from django.utils.text import slugify

def seed_cpp():
    course = Course.objects.get(slug='c-programming-advanced')
    
    print("Deleting existing C++ modules and questions...")
    Module.objects.filter(course=course).delete()
    
    print("Creating new modules...")
    modules = []
    names = [
        "Classes and Objects", "Array of Objects", "Dynamic Memory Allocation",
        "Dynamic Array Allocation", "Friend Functions", "Static Variables",
        "Static Member Functions", "Copy Constructors", "Operator Overloading",
        "Constructor Overloading", "Constructors in Derived Classes", "Hierarchical Inheritance",
        "Hybrid Inheritance", "Virtual Base Classes", "Templates"
    ]
    
    for i, name in enumerate(names):
        modules.append(Module.objects.create(
            name=name, course=course, category="c_programming_advanced", order=i+1, level=i+1
        ))

    print("Adding Mandatory Lab Manual Questions...")
    
    # M1: Classes and Objects
    q1 = Question.objects.create(
        module=modules[0], title="Box Volume", slug="box-volume",
        description="Write a C++ program to declare a class called `Box` with private data members `length`, `breadth`, and `height` and the public member functions `setLength()`, `setBreadth()`, `setHeight()`. Declare a pointer to class. Compute the volume of the two objects using `compVolume()` function.\n\nInput Format: 6 space-separated integers (L B H for Box 1, then L B H for Box 2).",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q1, is_sample=True, order=1, stdin="2 3 4\n3 4 5\n", expected_output="Volume 1: 24\nVolume 2: 60\n")
    TestCase.objects.create(question=q1, is_sample=False, order=2, stdin="5 5 5\n1 2 3\n", expected_output="Volume 1: 125\nVolume 2: 6\n")

    # M2: Array of Objects
    q2 = Question.objects.create(
        module=modules[1], title="Employee Salary", slug="employee-salary",
        description="Write a C++ program to read the data of N employees and compute the Net salary of each employee (DA=52% of Basic and Income Tax (IT) = 30% of the gross salary).\n\nFor that, create an `Employee` class with Employee number, Employee name, Basic, DA, IT, Net Salary.\n\nInput Format: N, then N lines of `Number Name Basic`.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q2, is_sample=True, order=1, stdin="2\n101 John 50000\n102 Alice 60000\n", expected_output="101 John 50000 26000 22800 53200\n102 Alice 60000 31200 27360 63840\n")

    # M3: Dynamic Memory
    q3 = Question.objects.create(
        module=modules[2], title="Square Area", slug="square-area",
        description="Write a C++ program to allocate memory dynamically for two objects. The name of the class is `Square` with a data member called `side` and a constructor called `Square(int)` and `compArea()` member function. Use `new` and `delete` operators for memory allocation and deallocation.\n\nInput Format: 2 integers for the sides of the two squares.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q3, is_sample=True, order=1, stdin="4 5\n", expected_output="Area 1: 16\nArea 2: 25\n")

    # M4: Dynamic Array
    q4 = Question.objects.create(
        module=modules[3], title="Student CGPA Sort", slug="student-cgpa-sort",
        description="Write a C++ program to allocate memory dynamically for an array. Read into the array the CGPA of N students and display the same in the sorted order. Use `new` and `delete` operators for memory allocation and deallocation.\n\nInput Format: N followed by N float values.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q4, is_sample=True, order=1, stdin="4\n7.5\n9.2\n8.1\n6.8\n", expected_output="6.8\n7.5\n8.1\n9.2\n")

    # M5: Friend Function
    q5 = Question.objects.create(
        module=modules[4], title="Maximum of Two Classes", slug="maximum-two-classes",
        description="Write a C++ program with two classes `ABC` and `XYZ` with one integer data member in each class. Write member functions to read and display, place a friend function called `max()` in these classes which takes the data members of these classes and computes a maximum of two data members. Demonstrate using the main() function.\n\nInput Format: Two integers.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q5, is_sample=True, order=1, stdin="10 25\n", expected_output="Maximum: 25\n")

    # M6: Static Variables
    q6 = Question.objects.create(
        module=modules[5], title="Integer Display", slug="integer-display",
        description="Write a C++ program to design a class called `IntegerDisplay` with both an integer variable and a static integer variable. Display both data using corresponding member functions namely `print_i()` and `print_si()`.\n\nInput Format: One integer to initialize.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q6, is_sample=True, order=1, stdin="42\n", expected_output="Integer: 42\nStatic Integer: 42\n")

    # M7: Static Functions
    q7 = Question.objects.create(
        module=modules[6], title="Object Counter", slug="object-counter",
        description="Write a Program to design a class having a static member function named `ShowCount()` which has the property of displaying the number of objects created of the class. Read N, create N objects, and display count.\n\nInput Format: Integer N.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q7, is_sample=True, order=1, stdin="5\n", expected_output="Count: 5\n")

    # M8: Copy Constructors
    q8 = Question.objects.create(
        module=modules[7], title="Point Copy", slug="point-copy",
        description="Write a C++ program to demonstrate the working of a copy constructor. Implement a class called `Point` with private data members X and Y as the points and `getX()` and `getY()` are the getter functions to get the values and print the same using the main() function.\n\nInput Format: Two integers X and Y.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q8, is_sample=True, order=1, stdin="10 20\n", expected_output="Original: 10, 20\nCopied: 10, 20\n")

    # M9: Operator Overloading
    q9 = Question.objects.create(
        module=modules[8], title="Complex Numbers Math", slug="complex-numbers-math",
        description="Write a C++ program to overload binary `+` and `-` operator to add and subtract two complex numbers. Define relevant data members and member functions for reading and displaying the complex objects.\n\nInput Format: Four integers representing (Real1, Imag1) and (Real2, Imag2).",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q9, is_sample=True, order=1, stdin="3 4\n1 2\n", expected_output="Sum: 4 + 6i\nDifference: 2 + 2i\n")

    # M10: Constructor Overloading
    q10 = Question.objects.create(
        module=modules[9], title="Data Class", slug="data-class",
        description="Write a C++ program to create a class `Data` with integer, character and float data members. Demonstrate Constructor Overloading on this class with all types of constructors including default argument constructor.\n\nInput: Integer, Char, Float.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q10, is_sample=True, order=1, stdin="10 A 3.14\n", expected_output="Int: 10\nChar: A\nFloat: 3.14\n")

    # M11: Derived Class Constructors
    q11 = Question.objects.create(
        module=modules[10], title="Alpha Beta Gamma", slug="alpha-beta-gamma",
        description="Write a C++ program to demonstrate the uses of constructors in derived class concepts. Classes `Alpha`, `Beta`, and `Gamma` in \"is-a\" relationship. Members `n1`, `n2`, `n3` with functions `putAlpha()`, `putBeta()`, `putGamma()`. Base class constructors must have at least one parameter.\n\nInput: Three integers.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q11, is_sample=True, order=1, stdin="1 2 3\n", expected_output="Alpha: 1\nBeta: 2\nGamma: 3\n")

    # M12: Hierarchical Inheritance
    q12 = Question.objects.create(
        module=modules[11], title="Student Streams", slug="student-streams",
        description="Write a C++ program using Hierarchical inheritance. Base: `Student` (name, USN, age, `getStudent()`). Childs: `Medical` (year, `getMedical()`, `display()`) and `Engineering` (sem, branch, `getEngineering()`, `display()`).\n\nInput: Medical Student details, then Engineering Student details.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q12, is_sample=True, order=1, stdin="Alice 101 20 2\nBob 102 19 3 CSE\n", expected_output="Medical: Alice 101 20 2\nEngineering: Bob 102 19 3 CSE\n")

    # M13: Hybrid Inheritance
    q13 = Question.objects.create(
        module=modules[12], title="Student Results", slug="student-results",
        description="Write a C++ program using Hybrid inheritance. `Student` -> `Test`. `Test` & `Sports` -> `Result`.\nInput: Name, USN, Sub1, Sub2, Sports Score.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q13, is_sample=True, order=1, stdin="Alice 101 80 90 85\n", expected_output="Name: Alice\nUSN: 101\nTotal: 255\n")

    # M14: Virtual Base Classes
    q14 = Question.objects.create(
        module=modules[13], title="Virtual Base Results", slug="virtual-base-results",
        description="Write a C++ program using Virtual Base class. `Student` -> `Test` and `Sports`. `Test` & `Sports` -> `Result`. Create an array of N objects of Result class.\n\nInput: N, then N lines of Name, USN, Sub1, Sub2, Sports Score.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q14, is_sample=True, order=1, stdin="2\nAlice 101 80 90 85\nBob 102 70 60 75\n", expected_output="Alice 101 255\nBob 102 205\n")

    # M15: Templates
    q15 = Question.objects.create(
        module=modules[14], title="Template Bubble Sort", slug="template-bubble-sort",
        description="Write a C++ program to apply bubble sort on an array of integers and float using the concept of function template.\n\nInput: N integers, then N floats.",
        difficulty="hard", csv_level=3, language_id=54, is_mandatory=True,
    )
    TestCase.objects.create(question=q15, is_sample=True, order=1, stdin="3\n3 1 2\n3.3 1.1 2.2\n", expected_output="1 2 3\n1.1 2.2 3.3\n")


    print("Mandatory questions added successfully.")
    print("Generating remaining questions for the pool using RAG (this will take a few minutes)...")
    
    # RAG Generation calls
    topics_list = [
        ["C++ basics, classes, access modifiers", "C++ object creation, encapsulation", "Pointers to classes, public vs private"],
        ["Arrays in C++, object arrays", "Iterating through arrays, C++ string", "Managing memory for arrays of objects"],
        ["new keyword, delete keyword", "Dynamic memory allocation for objects", "Constructors and dynamic allocation"],
        ["Dynamic array allocation", "Pointers and arrays", "Sorting arrays in C++, CGPA system"],
        ["Friend functions", "Friend classes", "Multiple classes, access protected members via friend"],
        ["Static variables in classes", "Global vs static", "Static data members C++"],
        ["Static member functions", "Calling static functions without objects", "Static vs instance methods"],
        ["Copy constructor in C++", "Deep copy vs shallow copy", "Passing objects by value"],
        ["Operator overloading", "Overloading binary operators", "Complex numbers implementation"],
        ["Constructor overloading", "Default arguments in constructors", "Multiple constructors"],
        ["Inheritance, derived class constructors", "is-a relationship, base initialization", "Constructor execution order"],
        ["Hierarchical inheritance", "Protected access modifier", "Multiple child classes in C++"],
        ["Hybrid inheritance, diamond problem", "Multiple inheritance", "Resolving ambiguity"],
        ["Virtual base classes", "virtual keyword inheritance", "Array of objects of derived class"],
        ["C++ function templates", "Class templates", "Generic programming, Bubble sort generic"]
    ]

    for i in range(15):
        call_command("bulk_generate_questions", topics=topics_list[i][0], difficulty="easy", module_id=modules[i].id)
        call_command("bulk_generate_questions", topics=topics_list[i][1], difficulty="medium", module_id=modules[i].id)
        call_command("bulk_generate_questions", topics=topics_list[i][2], difficulty="hard", module_id=modules[i].id)

    print("DONE! C++ Programming course has been completely re-seeded.")

seed_cpp()
