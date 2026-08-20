#!/usr/bin/env python3
"""Validate every question-bank JSON file against the canonical schema
(docs/QUESTION_JSON_SCHEMA.md) and optionally export flat JSONL for LLM training.

Usage:
  python3 scripts/validate_question_json.py                 # validate all files
  python3 scripts/validate_question_json.py --jsonl out.jsonl
"""
import argparse
import glob
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS = (
    sorted(glob.glob(os.path.join(BASE_DIR, "generated_level_question_csvs", "*.json")))
    + sorted(glob.glob(os.path.join(BASE_DIR, "data", "*.json")))
)

VALID_CATEGORIES = {"c_programming", "placement_training", "advanced_placement_training"}
VALID_DIFFICULTIES = {"easy", "medium", "hard"}
VALID_LEVEL_RANGES = {"", "Easy", "Medium", "Hard"}

QUESTION_REQUIRED = {
    "question_id", "title", "topic", "level", "level_range", "difficulty",
    "description", "starter_code", "time_limit", "memory_limit_kb", "max_score",
    "is_active", "is_mandatory", "allow_multiple_languages", "test_cases",
}
QUESTION_OPTIONAL = {"solution"}
TEST_REQUIRED = {"input", "expected_output", "is_sample"}
INT_FIELDS = {"level", "memory_limit_kb", "max_score"}
BOOL_FIELDS = {"is_active", "is_mandatory", "allow_multiple_languages"}


def validate_question(q, where, errors):
    missing = QUESTION_REQUIRED.difference(q.keys())
    if missing:
        errors.append(f"{where}: missing keys {sorted(missing)}")
        return
    unknown = set(q.keys()).difference(QUESTION_REQUIRED | QUESTION_OPTIONAL)
    if unknown:
        errors.append(f"{where}: unknown keys {sorted(unknown)}")
    if not isinstance(q["question_id"], str) or not q["question_id"].strip():
        errors.append(f"{where}: question_id must be a non-empty string")
    if not isinstance(q["title"], str) or not q["title"].strip():
        errors.append(f"{where}: title must be a non-empty string")
    if q["difficulty"] not in VALID_DIFFICULTIES:
        errors.append(f"{where}: difficulty {q['difficulty']!r} not in {sorted(VALID_DIFFICULTIES)}")
    if q["level_range"] not in VALID_LEVEL_RANGES:
        errors.append(f"{where}: level_range {q['level_range']!r} unexpected")
    for field in INT_FIELDS:
        if not isinstance(q[field], int) or isinstance(q[field], bool):
            errors.append(f"{where}: {field} must be an int, got {q[field]!r}")
    if not isinstance(q["time_limit"], (int, float)) or isinstance(q["time_limit"], bool):
        errors.append(f"{where}: time_limit must be numeric, got {q['time_limit']!r}")
    for field in BOOL_FIELDS:
        if not isinstance(q[field], bool):
            errors.append(f"{where}: {field} must be a bool, got {q[field]!r}")
    if not q["description"].strip():
        errors.append(f"{where}: empty description")

    cases = q["test_cases"]
    if not isinstance(cases, list) or not cases:
        errors.append(f"{where}: test_cases must be a non-empty list")
        return
    seen = set()
    samples = 0
    for i, tc in enumerate(cases, 1):
        tc_where = f"{where} test_cases[{i}]"
        if set(tc.keys()) != TEST_REQUIRED:
            errors.append(f"{tc_where}: keys must be exactly {sorted(TEST_REQUIRED)}, got {sorted(tc.keys())}")
            continue
        if not isinstance(tc["is_sample"], bool):
            errors.append(f"{tc_where}: is_sample must be a bool")
        elif tc["is_sample"]:
            samples += 1
        if not isinstance(tc["expected_output"], str):
            errors.append(f"{tc_where}: expected_output must be a string")
        key = (tc["input"], tc["expected_output"])
        if key in seen:
            errors.append(f"{tc_where}: exact duplicate of an earlier test case")
        seen.add(key)
    if samples < 1:
        errors.append(f"{where}: no test case flagged is_sample=true")


def validate_file(path):
    errors = []
    rel = os.path.relpath(path, BASE_DIR)
    try:
        with open(path, encoding="utf-8-sig") as fh:
            doc = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{rel}: cannot parse ({exc})"], 0, 0

    if not isinstance(doc, dict) or set(doc.keys()) != {"category", "modules"}:
        return [f"{rel}: top level must be {{'category', 'modules'}}"], 0, 0
    if doc["category"] not in VALID_CATEGORIES:
        errors.append(f"{rel}: category {doc['category']!r} not in {sorted(VALID_CATEGORIES)}")
    if not isinstance(doc["modules"], list) or not doc["modules"]:
        return errors + [f"{rel}: 'modules' must be a non-empty list"], 0, 0

    q_count = tc_count = 0
    ids = set()
    for m_idx, mod in enumerate(doc["modules"], 1):
        if set(mod.keys()) != {"module", "module_order", "questions"}:
            errors.append(f"{rel} modules[{m_idx}]: keys must be 'module', 'module_order', 'questions'")
            continue
        if not isinstance(mod["module"], str) or not mod["module"].strip():
            errors.append(f"{rel} modules[{m_idx}]: empty module name")
        if not isinstance(mod["module_order"], int) or isinstance(mod["module_order"], bool):
            errors.append(f"{rel} modules[{m_idx}]: module_order must be an int")
        for q_idx, q in enumerate(mod["questions"], 1):
            validate_question(q, f"{rel} modules[{m_idx}] questions[{q_idx}]", errors)
            q_count += 1
            tc_count += len(q.get("test_cases") or [])
            qid = q.get("question_id")
            if isinstance(qid, str):
                if qid in ids:
                    errors.append(f"{rel}: duplicate question_id {qid!r}")
                ids.add(qid)
    return errors, q_count, tc_count


def export_jsonl(out_path):
    rows = []
    for path in TARGETS:
        with open(path, encoding="utf-8-sig") as fh:
            doc = json.load(fh)
        for mod in doc["modules"]:
            for q in mod["questions"]:
                rows.append({
                    "category": doc["category"],
                    "module": mod["module"],
                    "module_order": mod["module_order"],
                    **q,
                })
    with open(out_path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Wrote {len(rows)} training examples to {out_path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jsonl", metavar="OUT", help="also export flat JSONL for LLM training")
    args = parser.parse_args()

    if not TARGETS:
        print("No question-bank JSON files found.", file=sys.stderr)
        sys.exit(1)

    total_errors = 0
    total_q = total_tc = 0
    for path in TARGETS:
        errors, q_count, tc_count = validate_file(path)
        total_q += q_count
        total_tc += tc_count
        rel = os.path.relpath(path, BASE_DIR)
        if errors:
            total_errors += len(errors)
            print(f"FAIL {rel} ({q_count} questions)")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"OK   {rel} ({q_count} questions, {tc_count} test cases)")

    print(f"\n{len(TARGETS)} files: {total_q} questions, {total_tc} test cases, {total_errors} errors.")
    if args.jsonl:
        if total_errors:
            print("Refusing --jsonl export: fix validation errors first.", file=sys.stderr)
            sys.exit(1)
        export_jsonl(args.jsonl)
    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
