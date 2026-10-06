from core.sandbox import run_code
import os

source_code = "SELECT * FROM students;"
stdin = "CREATE TABLE students (id INT, name TEXT);\nINSERT INTO students VALUES (1, 'Alice');"

result = run_code(
    language="sql",
    source_code=source_code,
    stdin=stdin,
    expected_output="1|Alice",
    time_limit=2.0
)
print("Result:", result)
