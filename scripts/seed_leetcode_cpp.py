import json
import sys
import os

sys.path.insert(0, '/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from django.utils.text import slugify
from core.models import Course, Module, Question, TestCase

def clean_description(desc):
    if not desc: return desc
    import re
    cleaned = re.sub(r'\nExample \d+:', '', desc)
    cleaned = re.sub(r'\nConstraints:', '', cleaned)
    return cleaned.strip()

def parse_example(text):
    lines = text.strip().split('\n')
    input_val, output_val = None, None
    for line in lines:
        line = line.strip()
        if line.startswith('Input:'):
            input_val = line[len('Input:'):].strip()
        elif line.startswith('Output:'):
            output_val = line[len('Output:'):].strip()
    return input_val, output_val

def difficulty_to_db(difficulty_str):
    mapping = {'Easy': Question.Difficulty.EASY, 'Medium': Question.Difficulty.MEDIUM, 'Hard': Question.Difficulty.HARD}
    return mapping.get(difficulty_str, Question.Difficulty.MEDIUM)

def main():
    course = Course.objects.get(slug='c-programming-advanced')
    modules = list(Module.objects.filter(course=course).order_by('order'))
    if not modules:
        print("No modules found!")
        return

    with open('/app/leetcode-problems-master/merged_problems.json') as f:
        data = json.load(f)

    # Filter for C++ problems with valid examples
    valid_qs = {'Easy': [], 'Medium': [], 'Hard': []}
    for p in data['questions']:
        if 'cpp' not in p.get('code_snippets', {}): continue
        # Must have at least one valid example
        valid = False
        for ex in p.get('examples', []):
            input_val, output_val = parse_example(ex.get('example_text', ''))
            if input_val and output_val:
                valid = True
                break
        if valid:
            diff = p.get('difficulty', 'Medium')
            if diff in valid_qs:
                valid_qs[diff].append(p)

    import random
    # To satisfy 5 easy, 4 med, 3 hard total (including 1 mandatory hard), we add 10 easy, 8 med, 4 hard per module
    per_module_targets = {'Easy': 10, 'Medium': 8, 'Hard': 4}

    total_created = 0
    for module in modules:
        print(f"Seeding module: {module.name}")
        for diff, target in per_module_targets.items():
            if not valid_qs[diff]: continue
            
            # Remove from pool so we don't duplicate questions if possible, 
            # but since pool is huge (800 easy), we can just sample without replacement.
            if len(valid_qs[diff]) >= target:
                selected = random.sample(valid_qs[diff], target)
                # Remove selected so they aren't reused in other modules
                valid_qs[diff] = [q for q in valid_qs[diff] if q not in selected]
            else:
                selected = valid_qs[diff]

            for p in selected:
                desc = clean_description(p.get('description', ''))
                base_slug = slugify(p.get('problem_slug', p['title']))[:160]
                slug = base_slug
                counter = 1
                while Question.objects.filter(module=module, slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1

                q = Question.objects.create(
                    module=module,
                    title=p['title'],
                    slug=slug,
                    description=desc,
                    difficulty=difficulty_to_db(p['difficulty']),
                    csv_level=2,
                    starter_code=p['code_snippets']['cpp'],
                    language_id=54, # C++
                    time_limit=2.0,
                    memory_limit_kb=128000,
                    allow_multiple_languages=False,
                    is_mandatory=False,
                    is_active=True,
                )
                
                # Test cases
                for idx, ex in enumerate(p.get('examples', []), start=1):
                    input_val, output_val = parse_example(ex.get('example_text', ''))
                    if input_val and output_val:
                        TestCase.objects.create(
                            question=q,
                            stdin=input_val,
                            expected_output=output_val,
                            is_sample=(idx == 1),
                            order=idx,
                        )
                total_created += 1

    print(f"Successfully seeded {total_created} extra C++ questions from LeetCode across {len(modules)} modules!")

if __name__ == '__main__':
    main()
