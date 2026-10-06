"""
Import LeetCode problems from leetcode-problems-master into the E-Lab database.
Selects 1500 problems with valid Input/Output examples, balanced across difficulties.
"""
import json
import re
import sys
import os

sys.path.insert(0, '/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from django.utils.text import slugify
from core.models import Module, Question, TestCase


def clean_description(desc):
    """Remove trailing 'Example N:' and 'Constraints:' fragments from description."""
    if not desc:
        return desc
    # Remove trailing example references and constraints label
    cleaned = re.sub(r'\nExample \d+:', '', desc)
    cleaned = re.sub(r'\nConstraints:', '', cleaned)
    return cleaned.strip()


def parse_example(text):
    """Extract input and output from a LeetCode example text."""
    lines = text.strip().split('\n')
    input_val = None
    output_val = None
    for line in lines:
        line = line.strip()
        if line.startswith('Input:'):
            input_val = line[len('Input:'):].strip()
        elif line.startswith('Output:'):
            output_val = line[len('Output:'):].strip()
    return input_val, output_val


def difficulty_to_db(difficulty_str):
    """Map LeetCode difficulty to DB enum."""
    mapping = {
        'Easy': Question.Difficulty.EASY,
        'Medium': Question.Difficulty.MEDIUM,
        'Hard': Question.Difficulty.HARD,
    }
    return mapping.get(difficulty_str, Question.Difficulty.MEDIUM)


def select_problems(questions, target_count=1500):
    """Select problems balanced across difficulties."""
    by_diff = {}
    for p in questions:
        d = p['difficulty']
        if d not in by_diff:
            by_diff[d] = []
        by_diff[d].append(p)

    # Count available per difficulty
    counts = {d: len(probs) for d, probs in by_diff.items()}
    print(f"Available problems: {counts}")

    # Target ~equal split, but cap at available
    target_per_diff = target_count // 3
    selected = []
    for diff in ['Easy', 'Medium', 'Hard']:
        available = by_diff.get(diff, [])
        take = min(target_per_diff, len(available))
        # Shuffle for randomness, then take
        import random
        random.shuffle(available)
        selected.extend(available[:take])

    print(f"Selected {len(selected)} problems")
    return selected


def main():
    # Load problems
    with open('/app/leetcode-problems-master/merged_problems.json') as f:
        data = json.load(f)
    all_questions = data['questions']
    print(f"Total LeetCode problems: {len(all_questions)}")

    # Filter to problems with at least one valid Input/Output example
    valid_questions = []
    for p in all_questions:
        for ex in p.get('examples', []):
            text = ex.get('example_text', '')
            lines = text.strip().split('\n')
            if any(l.startswith('Input:') for l in lines) and any(l.startswith('Output:') for l in lines):
                valid_questions.append(p)
                break

    print(f"Problems with valid examples: {len(valid_questions)}")

    # Select 1500
    selected = select_problems(valid_questions, 1500)

    # Get or create module
    try:
        module = Module.objects.get(pk=1)
    except Module.DoesNotExist:
        print("Module ID 1 not found. Creating...")
        module = Module.objects.create(
            name='DSA Practice',
            description='LeetCode-style DSA problems',
            level=1,
            order=1,
            category='c_programming',
        )
    print(f"Using module: {module.name} (ID: {module.pk})")

    # Track stats
    created = 0
    skipped = 0
    total_test_cases = 0

    for p in selected:
        # Clean description
        desc = clean_description(p.get('description', ''))

        # Parse examples into test cases
        test_cases = []
        for ex in p.get('examples', []):
            text = ex.get('example_text', '')
            input_val, output_val = parse_example(text)
            if input_val and output_val:
                test_cases.append({
                    'stdin': input_val,
                    'expected_output': output_val,
                    'is_sample': len(test_cases) == 0,  # First valid example is sample
                })

        if not test_cases:
            skipped += 1
            continue

        # Build slug
        base_slug = slugify(p.get('problem_slug', p['title']))[:160]
        slug = base_slug
        counter = 1
        while Question.objects.filter(module=module, slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        # Get C starter code
        c_code = p.get('code_snippets', {}).get('c', '')

        # Create question
        question = Question.objects.create(
            module=module,
            title=p['title'],
            slug=slug,
            description=desc,
            difficulty=difficulty_to_db(p['difficulty']),
            csv_level=1,
            level_range=p['difficulty'],
            starter_code=c_code,
            language_id=50,  # C (GCC)
            time_limit=2.0,
            memory_limit_kb=128000,
            allow_multiple_languages=False,
            is_mandatory=False,
            is_active=True,
        )

        # Create test cases
        for idx, tc in enumerate(test_cases, start=1):
            TestCase.objects.create(
                question=question,
                stdin=tc['stdin'],
                expected_output=tc['expected_output'],
                is_sample=tc['is_sample'],
                order=idx,
            )
            total_test_cases += 1

        created += 1
        if created % 100 == 0:
            print(f"  Created {created}/{len(selected)} questions, {total_test_cases} test cases")

    print(f"\n{'='*50}")
    print(f"Done! Created: {created}, Skipped: {skipped}, Test cases: {total_test_cases}")

    # Verify
    from django.db import models
    q_count = Question.objects.filter(module=module).count()
    tc_count = TestCase.objects.filter(question__module=module).count()
    print(f"Database totals - Questions: {q_count}, Test cases: {tc_count}")


if __name__ == '__main__':
    main()
