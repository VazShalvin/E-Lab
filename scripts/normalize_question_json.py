#!/usr/bin/env python3
"""Normalize every question-bank JSON file to the canonical E-Lab schema.

Canonical schema (see docs/QUESTION_JSON_SCHEMA.md):

{
  "category": "<module category slug>",
  "modules": [
    {
      "module": "<display name>",
      "module_order": <int>,
      "questions": [
        {
          "question_id": "E001",
          "title": "...",
          "topic": "...",
          "level": 1,
          "level_range": "Easy",
          "difficulty": "easy",
          "description": "...",
          "starter_code": "...",
          "time_limit": 2,
          "memory_limit_kb": 128000,
          "max_score": 1,
          "is_active": true,
          "is_mandatory": false,
          "allow_multiple_languages": false,
          "test_cases": [
            {"input": "...", "expected_output": "...", "is_sample": true}
          ]
        }
      ]
    }
  ]
}

Accepts legacy formats:
  A) week-keyed dict:  {"1": [{"title","desc","diff","test_cases":[{"in","out","is_sample"}]}]}
  B) CSV-row list:     [{"Question_ID","Title","Topic","Level",...,"Test1_Input","Test1_Output",...}]
  C) already-canonical files (idempotent re-normalization).

Usage: python3 scripts/normalize_question_json.py [--dry-run]
"""
import argparse
import glob
import json
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODULES_DIR = os.path.join(BASE_DIR, "generated_level_question_csvs")

DEFAULT_C_STARTER = (
    "#include <stdio.h>\n\n"
    "int main(void)\n"
    "{\n"
    "    /* Read from stdin. Do not print prompts unless required. */\n"
    "    return 0;\n"
    "}\n"
)

# Mirrors core/management/commands/seed_placement_training.py
PLACEMENT_WEEKS = {
    1: ("Week 1: Introduction to Programming", "Variables, Data Types, Operators"),
    2: ("Week 2: Decision Making and Looping", "Pattern printing, Prime, Armstrong"),
    3: ("Week 3: Logic Building & Workflows", "Flow Control, Arrays, Math Coding"),
    4: ("Week 4: Functions and Arrays", "Matrix operations, searching"),
    5: ("Week 5: Strings and Pointers", "Palindrome, string manipulation"),
    6: ("Week 6: Language Deep Dive & STL", "Collections, Clean Code"),
    7: ("Week 7: Structures & Recursion", "Structured programming"),
    8: ("Week 8: Searching and Sorting", "Linear/Binary search, sorting"),
    9: ("Week 9: Intro to Data Structures", "Stack, Queue, Linked List"),
    10: ("Week 10: Linked Lists & Recursion", "Insert/Delete/Search nodes"),
    11: ("Week 11: Competitive Programming", "Coding strategies, online practice"),
}

# Mirrors core/management/commands/seed_advanced_placement_training.py
ADVANCED_WEEKS = {
    1: ("Week 1: Complexity Analysis", "Revision of Programming Fundamentals, Complexity Analysis"),
    2: ("Week 2: Arrays and Strings", "Sliding Window, Prefix Sum, String manipulation problems"),
    3: ("Week 3: Recursion & Backtracking", "Sudoku, Maze, N-Queens, Divide & Conquer"),
    4: ("Week 4: Linked Lists & Stacks", "Reverse linked list, Stack using arrays, Queue implementation"),
    5: ("Week 5: Trees and BST", "Tree traversals, BST operations"),
    6: ("Week 6: Graphs and Heaps", "DFS/BFS Traversals, Priority Queues"),
    7: ("Week 7: Hashing and Searching", "Hash Maps, Frequency counting, Collision handling"),
    8: ("Week 8: Sorting, Greedy & DP", "Merge Sort, Quick Sort, DP basics, Knapsack"),
    9: ("Week 9: OOP & Design Patterns", "Classes, Objects, Inheritance, Polymorphism, LLD"),
    10: ("Week 10: OS Fundamentals", "Process vs Thread, CPU Scheduling, Synchronization, Deadlocks"),
}


def as_bool(value, default=False):
    text = str(value if value is not None else "").strip().lower()
    if text in {"1", "true", "yes", "y", "active"}:
        return True
    if text in {"0", "false", "no", "n", "inactive", "draft"}:
        return False
    return default


def as_int(value, default=1):
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return default


def as_float(value, default=2.0):
    try:
        return float(str(value).strip())
    except (TypeError, ValueError):
        return default


def normalize_difficulty(value):
    text = str(value or "").strip().lower()
    return text if text in {"easy", "medium", "hard"} else "easy"


def module_name_from_filename(filename):
    """Same naming rules as core.views.module_name_from_csv so DB modules stay stable."""
    stem = os.path.basename(filename).rsplit(".", 1)[0]
    match = re.match(r"Module(\d+)_(.+)", stem, re.IGNORECASE)
    if not match:
        name = re.sub(r"[_\s]+(?:Full|Levels)$", "", stem, flags=re.IGNORECASE)
        return name.replace("_", " ").strip(), 1
    order = int(match.group(1))
    raw_name = re.sub(r"[_\s]+(?:Full|Levels)$", "", match.group(2), flags=re.IGNORECASE)
    name = raw_name.replace("_", " ").replace("IO", "I/O").strip()
    name = name.replace("Operators Expressions", "Operators & Expressions")
    name = name.replace("Conditionals Loops", "Conditionals & Loops")
    return name, order


def dedupe_cases(cases):
    """Drop exact duplicate (input, output) pairs, keeping first occurrence."""
    seen = set()
    kept = []
    for case in cases:
        key = (case["input"], case["expected_output"])
        if key in seen:
            continue
        seen.add(key)
        kept.append(case)
    return kept


# ---------------------------------------------------------------- format B ---
def convert_csv_row(row, index):
    question_id = (row.get("Question_ID") or f"Q{index:03d}").strip()
    topic = (row.get("Topic") or "Question").strip()
    level = as_int(row.get("Level"), 1)
    title = (row.get("Title") or f"{question_id} - {topic} (Level {level})").strip()

    cases = []
    for i in range(1, 21):
        stdin = row.get(f"Test{i}_Input")
        expected = row.get(f"Test{i}_Output")
        if expected is None:
            expected = row.get(f"Test{i}_Expected_Output")
        if expected is None:
            continue
        if str(stdin or "").strip() == "" and str(expected).strip() == "":
            continue
        cases.append({
            "input": str(stdin or ""),
            "expected_output": str(expected),
            "is_sample": len(cases) == 0,
        })

    return {
        "question_id": question_id,
        "title": title,
        "topic": topic,
        "level": level,
        "level_range": (row.get("Level_Range") or "").strip(),
        "difficulty": normalize_difficulty(row.get("Difficulty")),
        "description": (row.get("Problem_Statement") or row.get("Description") or "").strip(),
        "starter_code": (row.get("Starter_Code") or "").strip() or DEFAULT_C_STARTER,
        "time_limit": as_float(row.get("Time_Limit"), 2.0),
        "memory_limit_kb": as_int(row.get("Memory_Limit_KB"), 128000),
        "max_score": as_int(row.get("Max_Score"), 1),
        "is_active": as_bool(row.get("Is_Active"), default=bool(cases)),
        "is_mandatory": as_bool(row.get("Is_Mandatory"), default=False),
        "allow_multiple_languages": False,
        "test_cases": dedupe_cases(cases),
    }


def normalize_module_bank(path):
    """generated_level_question_csvs/Module*.json -> canonical single-module file."""
    with open(path, encoding="utf-8-sig") as fh:
        rows = json.load(fh)
    if isinstance(rows, dict) and "modules" in rows:
        rows = rows["modules"][0]["questions"]  # already canonical, re-normalize
    name, order = module_name_from_filename(os.path.basename(path))
    questions = [convert_csv_row(row, i) for i, row in enumerate(rows, start=1)]
    return {
        "category": "c_programming",
        "modules": [{"module": name, "module_order": order, "questions": questions}],
    }


# ---------------------------------------------------------------- format A ---
def convert_week_item(item, week, seq, topic, id_prefix):
    difficulty = normalize_difficulty(item.get("diff") or item.get("difficulty"))
    raw_cases = item.get("test_cases") or []
    cases = []
    for idx, tc in enumerate(raw_cases):
        stdin = tc.get("input", tc.get("in", ""))
        expected = tc.get("expected_output", tc.get("out", ""))
        if str(expected or "") == "":
            continue
        cases.append({
            "input": str(stdin or ""),
            "expected_output": str(expected),
            "is_sample": bool(tc.get("is_sample", idx == 0)),
        })
    return {
        "question_id": f"{id_prefix}-W{week}-Q{seq:02d}",
        "title": (item.get("title") or f"{id_prefix} Week {week} Question {seq}").strip(),
        "topic": topic,
        "level": week,
        "level_range": difficulty.capitalize(),
        "difficulty": difficulty,
        "description": (item.get("desc") or item.get("description") or "").strip(),
        "starter_code": (item.get("starter_code") or "").strip() or DEFAULT_C_STARTER,
        "time_limit": 2.0,
        "memory_limit_kb": 128000,
        "max_score": 1,
        "is_active": True,
        "is_mandatory": True,
        "allow_multiple_languages": True,
        "test_cases": dedupe_cases(cases),
    }


def normalize_week_bank(path, category, week_table, id_prefix):
    """data/placement_training_questions.json style -> canonical multi-module file."""
    with open(path, encoding="utf-8-sig") as fh:
        weeks_data = json.load(fh)
    modules = []
    for key in sorted(weeks_data.keys(), key=lambda k: as_int(k, 0)):
        week = as_int(key)
        week_name, topic = week_table.get(week, (f"Week {week}", "General"))
        questions = [
            convert_week_item(item, week, seq, topic, id_prefix)
            for seq, item in enumerate(weeks_data[key], start=1)
        ]
        if not questions:
            continue
        modules.append({"module": week_name, "module_order": week, "questions": questions})
    return {"category": category, "modules": modules}


def canonicalize(path):
    """Detect format and return the canonical structure for one file."""
    with open(path, encoding="utf-8-sig") as fh:
        data = json.load(fh)

    if isinstance(data, dict) and "modules" in data:
        # Already canonical: re-run through converters for idempotency.
        category = data.get("category", "c_programming")
        modules = []
        for mod in data["modules"]:
            if category == "placement_training":
                table, prefix = PLACEMENT_WEEKS, "PT"
            elif category == "advanced_placement_training":
                table, prefix = ADVANCED_WEEKS, "ADV"
            else:
                table, prefix = {}, None
            if prefix:
                week = as_int(mod.get("module_order"), 1)
                _, topic = table.get(week, (mod.get("module"), "General"))
                questions = [
                    convert_week_item(item, week, seq, topic, prefix)
                    for seq, item in enumerate(mod["questions"], start=1)
                ]
            else:
                questions = [
                    convert_csv_row(
                        {
                            "Question_ID": q["question_id"],
                            "Title": q["title"],
                            "Topic": q.get("topic"),
                            "Level": q.get("level"),
                            "Level_Range": q.get("level_range"),
                            "Difficulty": q.get("difficulty"),
                            "Problem_Statement": q.get("description"),
                            "Starter_Code": q.get("starter_code"),
                            "Time_Limit": q.get("time_limit"),
                            "Memory_Limit_KB": q.get("memory_limit_kb"),
                            "Max_Score": q.get("max_score"),
                            "Is_Active": q.get("is_active"),
                            "Is_Mandatory": q.get("is_mandatory"),
                            **{f"Test{i}_Input": c["input"] for i, c in enumerate(q.get("test_cases", []), 1)},
                            **{f"Test{i}_Output": c["expected_output"] for i, c in enumerate(q.get("test_cases", []), 1)},
                        },
                        idx,
                    )
                    for idx, q in enumerate(mod["questions"], start=1)
                ]
            modules.append({
                "module": mod.get("module"),
                "module_order": as_int(mod.get("module_order"), 1),
                "questions": questions,
            })
        return {"category": category, "modules": modules}

    if isinstance(data, list):
        return normalize_module_bank(path)

    if isinstance(data, dict):
        basename = os.path.basename(path)
        if "advanced" in basename:
            return normalize_week_bank(path, "advanced_placement_training", ADVANCED_WEEKS, "ADV")
        return normalize_week_bank(path, "placement_training", PLACEMENT_WEEKS, "PT")

    raise ValueError(f"Unrecognized JSON structure in {path}")


def count_tests(doc):
    return sum(len(m["questions"]) for m in doc["modules"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Report without writing files")
    args = parser.parse_args()

    targets = sorted(glob.glob(os.path.join(MODULES_DIR, "*.json"))) + sorted(glob.glob(os.path.join(DATA_DIR, "*.json")))
    if not targets:
        print("No question-bank JSON files found.", file=sys.stderr)
        sys.exit(1)

    total_q, total_tc, total_dupes = 0, 0, 0
    for path in targets:
        with open(path, encoding="utf-8-sig") as fh:
            before = json.load(fh)
        doc = canonicalize(path)
        raw_cases = 0
        if isinstance(before, dict) and "modules" in before:
            raw_cases = sum(len(q.get("test_cases", [])) for m in before["modules"] for q in m["questions"])
        elif isinstance(before, list):
            raw_cases = sum(
                1 for row in before for i in range(1, 21) if row.get(f"Test{i}_Output") is not None
            )
        else:
            raw_cases = sum(
                len(item.get("test_cases", [])) for v in before.values() for item in v
            )

        kept_cases = sum(len(q["test_cases"]) for m in doc["modules"] for q in m["questions"])
        dupes = raw_cases - kept_cases
        total_q += count_tests(doc)
        total_tc += kept_cases
        total_dupes += dupes
        rel = os.path.relpath(path, BASE_DIR)
        print(f"{rel}: {count_tests(doc)} questions, {kept_cases} test cases"
              + (f" (dropped {dupes} exact duplicates)" if dupes else ""))
        if not args.dry_run:
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(doc, fh, indent=2, ensure_ascii=False)
                fh.write("\n")

    print(f"\nTotal: {total_q} questions, {total_tc} test cases, {total_dupes} duplicates dropped.")
    if args.dry_run:
        print("Dry run: no files written.")


if __name__ == "__main__":
    main()
