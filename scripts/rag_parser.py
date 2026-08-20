import re
import json
from pathlib import Path
from db import init_db, get_conn
from config import REPO_PATH


def clean_topic_name(dirname: str) -> str:
    """Convert '01_Array' or '11_Dynamic_Programming' to 'array' or 'dynamic programming'."""
    # Remove leading numbers and underscores (e.g., "01_" -> "")
    name = re.sub(r'^\d+_', '', dirname)
    # Replace underscores with spaces
    name = name.replace('_', ' ').lower()
    return name


def parse_markdown_file(filepath: Path, topic: str):
    """Extract problem metadata from a LeetCode-style .md file."""
    content = filepath.read_text(encoding="utf-8", errors="ignore")

    # Title: First H1 heading (# Title) or filename
    title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else filepath.stem.replace('_', ' ').title()

    # Problem description: Everything between the title and the first ## heading
    # (or first code block)
    desc_match = re.search(r'^#\s+.*?\n(.*?)(?=\n##|\n```)', content, re.DOTALL | re.MULTILINE)
    problem_desc = desc_match.group(1).strip() if desc_match else ""

    # Solution code: Extract all Python code blocks
    code_blocks = re.findall(r'```python\s*\n(.*?)```', content, re.DOTALL)
    solution_code = "\n\n".join(code_blocks).strip() if code_blocks else ""

    # Test cases: Look for "## Examples" or "Input/Output" patterns
    test_cases = []

    # Try to find "Input: ... Output: ..." patterns
    tc_matches = re.findall(r'Input:\s*(.*?)\s*Output:\s*(.*?)(?=\n\n|\nInput:|\n##|\Z)', content, re.DOTALL)
    for inp, out in tc_matches:
        test_cases.append({
            "input": inp.strip().replace('*', ''),
            "expected": out.strip().replace('*', '')
        })

    # Difficulty heuristic from filename or content
    difficulty = "unknown"
    content_lower = content.lower()
    if "easy" in content_lower or "easy" in filepath.stem.lower():
        difficulty = "easy"
    elif "medium" in content_lower or "medium" in filepath.stem.lower():
        difficulty = "medium"
    elif "hard" in content_lower or "hard" in filepath.stem.lower():
        difficulty = "hard"

    return {
        "topic": topic,
        "filename": filepath.name,
        "title": title,
        "problem_desc": problem_desc,
        "solution_code": solution_code,
        "test_cases": json.dumps(test_cases),
        "difficulty": difficulty,
    }


def ingest_repo(repo_path: str = REPO_PATH):
    init_db()
    repo = Path(repo_path)

    if not repo.exists():
        print(f"ERROR: Repo path '{repo_path}' does not exist.")
        return

    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM repo_questions")  # Clear old data

    count = 0
    # Iterate through topic directories (e.g., 01_Array, 02_String)
    for topic_dir in sorted(repo.iterdir()):
        if not topic_dir.is_dir():
            continue

        topic = clean_topic_name(topic_dir.name)  # "01_Array" -> "array"

        # Process all markdown files in this topic directory
        for mdfile in sorted(topic_dir.glob("*.md")):
            # Skip README.md files in subfolders
            if mdfile.name.lower() == "readme.md":
                continue

            try:
                data = parse_markdown_file(mdfile, topic)
                cur.execute(
                    """
                    INSERT INTO repo_questions
                    (topic, filename, title, problem_desc, solution_code, test_cases, difficulty)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        data["topic"],
                        data["filename"],
                        data["title"],
                        data["problem_desc"],
                        data["solution_code"],
                        data["test_cases"],
                        data["difficulty"],
                    ),
                )
                count += 1
            except Exception as e:
                print(f"  SKIP {mdfile.name}: {e}")

    conn.commit()
    conn.close()
    print(f"Done. Parsed {count} markdown questions into SQLite.")


if __name__ == "__main__":
    ingest_repo()
