import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Course, Module, Question, TestCase
from django.contrib.auth import get_user_model

User = get_user_model()
admin_user = User.objects.filter(is_superuser=True).first()

def create_dbms_course():
    course, created = Course.objects.get_or_create(
        slug="dbms-sql",
        defaults={
            "name": "Database Management Systems (SQL)",
            "description": "Master database design, constraints, and SQL queries from basics to complex joins.",
            "year": 2,
            "semester": 4,
            "available_from_semester": 4,
            "is_active": True,
            "proctoring_enabled": False
        }
    )

    if not created:
        print("Course already exists, cleaning up modules...")
        course.modules.all().delete()

    modules_data = [
        ("Module 1: Basics of SQL", "Learn how to retrieve data, use basic WHERE clauses, and sort results.", 1, Question.Difficulty.EASY),
        ("Module 2: Aggregations & Grouping", "Master aggregate functions like COUNT, SUM, AVG and GROUP BY clauses.", 2, Question.Difficulty.MEDIUM),
        ("Module 3: Joins & Subqueries", "Work with multiple tables, INNER/LEFT joins, and nested subqueries.", 3, Question.Difficulty.HARD),
    ]

    for mod_name, mod_desc, order, difficulty in modules_data:
        module = Module.objects.create(
            name=mod_name,
            description=mod_desc,
            level=order,
            order=order,
            is_active=True,
            category="dbms-sql",
            course=course
        )

        for i in range(1, 6):
            q_title = f"{mod_name.split(':')[0]} - Question {i}"
            
            # Simple setup for basic module
            if order == 1:
                stdin_sql = "CREATE TABLE students (id INT, name TEXT, marks INT);\nINSERT INTO students VALUES (1, 'Alice', 85), (2, 'Bob', 90), (3, 'Charlie', 70), (4, 'David', 95);"
                if i == 1:
                    desc = "Write a query to retrieve all columns from the `students` table."
                    expected_output = "1|Alice|85\n2|Bob|90\n3|Charlie|70\n4|David|95\n"
                    starter = "SELECT * FROM students;"
                elif i == 2:
                    desc = "Write a query to retrieve only the `name` column from the `students` table."
                    expected_output = "Alice\nBob\nCharlie\nDavid\n"
                    starter = "-- Write your query here\n"
                elif i == 3:
                    desc = "Write a query to retrieve students who scored more than 80 marks."
                    expected_output = "1|Alice|85\n2|Bob|90\n4|David|95\n"
                    starter = "-- Write your query here\n"
                elif i == 4:
                    desc = "Write a query to retrieve students ordered by their marks in descending order."
                    expected_output = "4|David|95\n2|Bob|90\n1|Alice|85\n3|Charlie|70\n"
                    starter = "-- Write your query here\n"
                else:
                    desc = "Write a query to find the student with id = 3."
                    expected_output = "3|Charlie|70\n"
                    starter = "-- Write your query here\n"
                    
            elif order == 2:
                stdin_sql = "CREATE TABLE employees (id INT, department TEXT, salary INT);\nINSERT INTO employees VALUES (1, 'HR', 5000), (2, 'IT', 7000), (3, 'IT', 8000), (4, 'Sales', 6000), (5, 'HR', 5500);"
                if i == 1:
                    desc = "Write a query to count the total number of employees."
                    expected_output = "5\n"
                    starter = "-- Write your query here\n"
                elif i == 2:
                    desc = "Write a query to find the maximum salary among all employees."
                    expected_output = "8000\n"
                    starter = "-- Write your query here\n"
                elif i == 3:
                    desc = "Write a query to find the total salary paid in the IT department."
                    expected_output = "15000\n"
                    starter = "-- Write your query here\n"
                elif i == 4:
                    desc = "Write a query to list each department along with the number of employees in it. Order by department name."
                    expected_output = "HR|2\nIT|2\nSales|1\n"
                    starter = "-- Write your query here\n"
                else:
                    desc = "Write a query to find departments with an average salary greater than 5500."
                    expected_output = "IT\nSales\n"
                    starter = "-- Write your query here\n"

            else:
                stdin_sql = "CREATE TABLE customers (id INT, name TEXT);\nCREATE TABLE orders (id INT, customer_id INT, amount INT);\nINSERT INTO customers VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');\nINSERT INTO orders VALUES (101, 1, 200), (102, 1, 300), (103, 2, 500);"
                if i == 1:
                    desc = "Write a query to join customers and orders, showing customer name and order amount."
                    expected_output = "Alice|200\nAlice|300\nBob|500\n"
                    starter = "-- Write your query here\n"
                elif i == 2:
                    desc = "Write a query using a LEFT JOIN to show all customers and their order amounts (if any). Ensure customers with no orders show empty order values."
                    expected_output = "Alice|200\nAlice|300\nBob|500\nCharlie|\n"
                    starter = "-- Write your query here\n"
                elif i == 3:
                    desc = "Write a query to find the total amount spent by each customer (name and total amount). Order by name."
                    expected_output = "Alice|500\nBob|500\nCharlie|\n"
                    starter = "-- Write your query here\n"
                elif i == 4:
                    desc = "Write a subquery to find the names of customers who have placed at least one order."
                    expected_output = "Alice\nBob\n"
                    starter = "-- Write your query here\n"
                else:
                    desc = "Write a query to find customers who have NOT placed any orders."
                    expected_output = "Charlie\n"
                    starter = "-- Write your query here\n"

            q = Question.objects.create(
                module=module,
                title=q_title,
                slug=f"dbms-m{order}-q{i}",
                description=f"### Database Schema\n\n```sql\n{stdin_sql}\n```\n\n### Task\n\n{desc}",
                difficulty=difficulty,
                language_id=82, # SQL
                starter_code=starter,
                created_by=admin_user
            )

            TestCase.objects.create(
                question=q,
                stdin=stdin_sql,
                expected_output=expected_output.strip(),
                is_sample=True,
                order=1
            )
            # Add one hidden testcase so it has >=1 hidden (often platforms require this, but for SQL it's fine if it's just the same data or different data)
            TestCase.objects.create(
                question=q,
                stdin=stdin_sql,
                expected_output=expected_output.strip(),
                is_sample=False,
                order=2
            )

    print("DBMS course and questions created successfully!")

create_dbms_course()
