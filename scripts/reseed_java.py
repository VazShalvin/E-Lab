import os
import sys

from core.models import Course, Module, Question, TestCase
from django.core.management import call_command
from django.utils.text import slugify

def seed_java():
    course = Course.objects.get(slug='java-programming')
    
    print("Deleting existing Java modules and questions...")
    Module.objects.filter(course=course).delete()
    
    print("Creating new modules...")
    m1 = Module.objects.create(name="Classes & Objects", course=course, category="java_programming", order=1, level=1)
    m2 = Module.objects.create(name="Inheritance & Polymorphism", course=course, category="java_programming", order=2, level=2)
    m3 = Module.objects.create(name="Multithreading & Exceptions", course=course, category="java_programming", order=3, level=3)
    m4 = Module.objects.create(name="Collections & File Handling", course=course, category="java_programming", order=4, level=4)
    
    print("Adding Mandatory Lab Manual Questions...")
    
    # Q1: Resume (Module 1, Hard, Mandatory)
    q1 = Question.objects.create(
        module=m1,
        title="Generate Resume (Interface)",
        slug="generate-resume-interface",
        description="Write a program to generate a resume. Create an interface `Resume` with a method `biodata()`. Create 2 Java classes `Teacher` (data: personal information, qualification, experience, achievements) and `Student` (data: personal information, result, discipline) which implement the `Resume` interface.\n\nRead a string (either 'Teacher' or 'Student') and then read their respective details on following lines. Print their resume.",
        difficulty="hard",
        csv_level=3,
        language_id=62,
        is_mandatory=True,
        starter_code="""import java.util.Scanner;

interface Resume {
    void biodata();
}

// Write your classes here

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Implement input logic
    }
}"""
    )
    TestCase.objects.create(question=q1, is_sample=True, order=1,
        stdin="Teacher\nJohn Doe\nPh.D\n10 years\nBest Teacher Award\n",
        expected_output="Teacher Resume:\nName: John Doe\nQualification: Ph.D\nExperience: 10 years\nAchievements: Best Teacher Award\n")
    TestCase.objects.create(question=q1, is_sample=False, order=2,
        stdin="Student\nAlice\n9.8 CGPA\nComputer Science\n",
        expected_output="Student Resume:\nName: Alice\nResult: 9.8 CGPA\nDiscipline: Computer Science\n")

    # Q2: N Student Objects (Module 1, Hard, Mandatory)
    q2 = Question.objects.create(
        module=m1,
        title="N Student Objects",
        slug="n-student-objects",
        description="Create a Java class called `Student` with private instance variables: `USN`, `Name`, `Branch`, `Phone`. Write a Java program to read `N` (number of students) followed by their details. Create `N` Student objects and print their details in a tabular format (values separated by a single space, headers: `USN Name Branch Phone`).",
        difficulty="hard",
        csv_level=3,
        language_id=62,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q2, is_sample=True, order=1,
        stdin="2\n1RN21CS001 Alice CSE 9876543210\n1RN21CS002 Bob ECE 9876543211\n",
        expected_output="USN Name Branch Phone\n1RN21CS001 Alice CSE 9876543210\n1RN21CS002 Bob ECE 9876543211\n")

    # Q3: Staff Inheritance (Module 2, Hard, Mandatory)
    q3 = Question.objects.create(
        module=m2,
        title="Staff Inheritance",
        slug="staff-inheritance",
        description="Design a superclass called `Staff` with details: `StaffId`, `Name`, `Phone`, `Salary`. Extend this class by writing three subclasses: `Teaching` (domain, publications), `Technical` (skills), and `Contract` (period). Read details for one Teaching, one Technical, and one Contract staff (in that order) and display them.",
        difficulty="hard",
        csv_level=3,
        language_id=62,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q3, is_sample=True, order=1,
        stdin="101 Alice 999 50000 CS 5\n102 Bob 888 40000 Networking\n103 Charlie 777 30000 3-years\n",
        expected_output="Teaching: 101 Alice 999 50000 CS 5\nTechnical: 102 Bob 888 40000 Networking\nContract: 103 Charlie 777 30000 3-years\n")

    # Q4: Multilevel Inheritance (Module 2, Hard, Mandatory)
    q4 = Question.objects.create(
        module=m2,
        title="Multilevel Inheritance",
        slug="multilevel-inheritance",
        description="Write a Java program to demonstrate multilevel inheritance (at least four levels). Create classes: `Animal` -> `Mammal` -> `Dog` -> `Puppy`. Each class should have a method that prints its name (e.g., `Animal eats`, `Mammal walks`, `Dog barks`, `Puppy plays`). Instantiate `Puppy` and call all 4 methods in order.",
        difficulty="hard",
        csv_level=3,
        language_id=62,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q4, is_sample=True, order=1,
        stdin="",
        expected_output="Animal eats\nMammal walks\nDog barks\nPuppy plays\n")

    # Q5: Even and Odd Threads (Module 3, Hard, Mandatory)
    q5 = Question.objects.create(
        module=m3,
        title="Even and Odd Threads",
        slug="even-and-odd-threads",
        description="Write a Java program to print the sum of even numbers and the sum of odd numbers up to `N` using two threads. Implement one using the `Runnable` interface (for Even) and the other using the `Thread` class (for Odd). The main thread must `join()` them and print the final sums: `Even Sum: X` and `Odd Sum: Y`.",
        difficulty="hard",
        csv_level=3,
        language_id=62,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q5, is_sample=True, order=1,
        stdin="5\n",
        expected_output="Even Sum: 6\nOdd Sum: 9\n")
    TestCase.objects.create(question=q5, is_sample=False, order=2,
        stdin="10\n",
        expected_output="Even Sum: 30\nOdd Sum: 25\n")

    # Q6: Thread Synchronization (Module 3, Hard, Mandatory)
    q6 = Question.objects.create(
        module=m3,
        title="Thread Synchronization",
        slug="thread-synchronization",
        description="Develop a multithreaded java program to demonstrate synchronisation of a method. The method prints a message by embedding square brackets around it (e.g., `[Message]`). To pass the automated test cases, ensure you start and join the threads such that the output is exactly:\n[Learn]\n[Java]\n[Programming]",
        difficulty="hard",
        csv_level=3,
        language_id=62,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q6, is_sample=True, order=1,
        stdin="",
        expected_output="[Learn]\n[Java]\n[Programming]\n")

    # Q7: ArrayList and LinkedList (Module 4, Hard, Mandatory)
    q7 = Question.objects.create(
        module=m4,
        title="ArrayList and LinkedList Operations",
        slug="arraylist-and-linkedlist",
        description="Perform operations on `ArrayList` and `LinkedList` of Strings. Read `N` strings into an ArrayList, then read `M` strings into a LinkedList. Print both lists on separate lines (using standard `toString()`). Then, append 'End' to the LinkedList, update the 0th element of ArrayList to 'Start', and print both again.",
        difficulty="hard",
        csv_level=3,
        language_id=62,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q7, is_sample=True, order=1,
        stdin="2\nApple\nBanana\n2\nCat\nDog\n",
        expected_output="[Apple, Banana]\n[Cat, Dog]\n[Start, Banana]\n[Cat, Dog, End]\n")

    # Q8: File Handling Equivalent (Module 4, Hard, Mandatory)
    q8 = Question.objects.create(
        module=m4,
        title="Count Characters, Words, Lines",
        slug="count-chars-words-lines",
        description="Write a program that counts the number of characters, words, and lines in a given text. Words are separated by white-space. Read all lines from standard input until EOF. Print:\nLines: X\nWords: Y\nChars: Z",
        difficulty="hard",
        csv_level=3,
        language_id=62,
        is_mandatory=True,
    )
    TestCase.objects.create(question=q8, is_sample=True, order=1,
        stdin="Hello World\nThis is a test file.\n",
        expected_output="Lines: 2\nWords: 7\nChars: 33\n")


    print("Mandatory questions added successfully.")

    print("Generating remaining questions for the pool using RAG (this will take a few minutes)...")
    
    # Module 1
    call_command("bulk_generate_questions", topics="Class definition in Java,Creating objects in Java,Constructors in Java,this keyword,Method overloading,Access modifiers in Java", difficulty="easy", module_id=m1.id)
    call_command("bulk_generate_questions", topics="Encapsulation in Java,Copy constructor in Java,Array of objects in Java,Passing objects to methods,Returning objects from methods", difficulty="medium", module_id=m1.id)
    call_command("bulk_generate_questions", topics="Singleton class in Java,Complex number class implementation", difficulty="hard", module_id=m1.id)

    # Module 2
    call_command("bulk_generate_questions", topics="Single inheritance in Java,Multilevel inheritance basics,Method overriding in Java,super keyword in Java,final keyword in Java", difficulty="easy", module_id=m2.id)
    call_command("bulk_generate_questions", topics="Abstract classes in Java,Interfaces in Java,Multiple inheritance using interfaces,Runtime polymorphism in Java", difficulty="medium", module_id=m2.id)
    call_command("bulk_generate_questions", topics="Interface inheritance in Java,Abstract class vs Interface implementation", difficulty="hard", module_id=m2.id)

    # Module 3
    call_command("bulk_generate_questions", topics="Thread class in Java,Runnable interface in Java,Thread sleep method,Thread priority in Java,try catch block in Java", difficulty="easy", module_id=m3.id)
    call_command("bulk_generate_questions", topics="Multiple catch blocks in Java,throw and throws keyword,Custom exception in Java,Thread join method,Thread lifecycle in Java", difficulty="medium", module_id=m3.id)
    call_command("bulk_generate_questions", topics="Inter-thread communication in Java,Deadlock creation in Java", difficulty="hard", module_id=m3.id)

    # Module 4
    call_command("bulk_generate_questions", topics="ArrayList basic operations,LinkedList basic operations,HashSet in Java,HashMap in Java,Reading user input using Scanner", difficulty="easy", module_id=m4.id)
    call_command("bulk_generate_questions", topics="Iterating through HashMap,Sorting an ArrayList in Java,String manipulation in Java,StringBuilder usage,Comparable interface in Java", difficulty="medium", module_id=m4.id)
    call_command("bulk_generate_questions", topics="Comparator interface in Java,Serialization and Deserialization in Java", difficulty="hard", module_id=m4.id)

    print("DONE! Java Programming course has been completely re-seeded.")

seed_java()
