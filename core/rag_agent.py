"""
RAG Question Agent — generates C programming questions by adapting
problems from the local DSA knowledge base (data/DSA_Topics/).
No external LLM required; fully offline and fast (~1s per question).
"""

import logging
import math
import os
import random
import re
from pathlib import Path
from typing import List, Dict, Any, Tuple
from django.conf import settings

logger = logging.getLogger(__name__)

BASE_DIR = getattr(settings, 'BASE_DIR', Path(__file__).resolve().parent.parent)
DSA_TOPICS_DIR = Path(os.path.join(BASE_DIR, 'data', 'DSA_Topics'))


class RAGQuestionAgent:
    _instance = None
    _questions_cache = None

    def __init__(self, topics_dir: str = DSA_TOPICS_DIR):
        self.topics_dir = Path(topics_dir)
        self.questions: List[Dict[str, Any]] = []
        self._load_questions()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _clean_topic_name(self, dirname: str) -> str:
        name = re.sub(r'^\d+_', '', dirname)
        return name.replace('_', ' ').lower()

    def _clean_tc_value(text):
        """Strip markdown artifacts from test case input/output values."""
        if not text:
            return ''
        text = text.strip()
        text = re.sub(r'```(?:python|c|cpp|java|text)?\s*', '', text)
        text = re.sub(r'```', '', text)
        text = re.sub(r'\*+\s*', '', text)
        text = re.sub(r'\s*\*+', '', text)
        return text.strip()

    def _parse_markdown_file(self, filepath: Path, topic: str) -> Dict[str, Any]:
        content = filepath.read_text(encoding="utf-8", errors="ignore")

        # Extract title
        title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filepath.stem.replace('_', ' ').title()

        # Extract description
        desc_match = re.search(r'^#\s+.*?\n(.*?)(?=\n##|\n```)', content, re.DOTALL | re.MULTILINE)
        problem_desc = desc_match.group(1).strip() if desc_match else content[:600]

        # Extract code blocks
        code_blocks = re.findall(r'```(?:python|c|cpp|java)?\s*\n(.*?)```', content, re.DOTALL)
        solution_code = "\n\n".join(code_blocks).strip() if code_blocks else ""

        # Extract test cases/examples — try both markdown formats
        test_cases = []
        # Format 1: **Input:** / **Output:** with code blocks (DSA_Topics style)
        tc_matches = re.findall(
            r'\*\*Input:\s*\*\*\s*\n```(?:\w+)?\s*\n(.*?)\n```\s*\n\*\*Output:\s*\*\*\s*\n```(?:\w+)?\s*\n(.*?)\n```',
            content, re.DOTALL
        )
        # Format 2: Input: / Output: plain or with code blocks (LeetCode style fallback)
        if not tc_matches:
            tc_matches = re.findall(
                r'Input:\s*(.*?)\s*Output:\s*(.*?)(?=\n\n|\nInput:|\n##|\Z)',
                content, re.DOTALL
            )
        for inp, out in tc_matches:
            clean_inp = self._clean_tc_value(inp)
            clean_out = self._clean_tc_value(out)
            if clean_inp and clean_out:
                test_cases.append({
                    "input": clean_inp,
                    "expected": clean_out,
                })

        difficulty = "medium"
        content_lower = content.lower()
        if "easy" in content_lower:
            difficulty = "easy"
        elif "hard" in content_lower:
            difficulty = "hard"

        return {
            "id": f"{topic}_{filepath.stem}",
            "topic": topic,
            "filename": filepath.name,
            "title": title,
            "description": problem_desc,
            "solution_code": solution_code,
            "test_cases": test_cases,
            "difficulty": difficulty,
            "full_content": content
        }

    def _load_questions(self):
        if RAGQuestionAgent._questions_cache is not None:
            self.questions = RAGQuestionAgent._questions_cache
            return

        parsed = []
        if self.topics_dir.exists():
            for topic_dir in sorted(self.topics_dir.iterdir()):
                if not topic_dir.is_dir():
                    continue
                topic_name = self._clean_topic_name(topic_dir.name)
                for mdfile in sorted(topic_dir.glob("*.md")):
                    if mdfile.name.lower() == "readme.md":
                        continue
                    try:
                        q_data = self._parse_markdown_file(mdfile, topic_name)
                        parsed.append(q_data)
                    except Exception as e:
                        logger.debug(f"Failed to parse {mdfile}: {e}")

        self.questions = parsed
        RAGQuestionAgent._questions_cache = parsed
        logger.info(f"Loaded {len(parsed)} problems from {self.topics_dir}")

    def list_topics(self) -> List[str]:
        topics = sorted(list(set(q["topic"] for q in self.questions)))
        return topics if topics else [
            "array", "string", "linked list", "stack", "queue",
            "binary trees", "binary search", "heap", "hash map",
            "graph bfs dfs", "dynamic programming", "backtracking",
            "greedy", "two pointers", "bit manipulation", "sorting"
        ]

    def retrieve_similar(self, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        if not self.questions:
            return []

        query_tokens = set(re.findall(r'\w+', query.lower()))
        if not query_tokens:
            return self.questions[:n_results]

        scored_questions = []
        for q in self.questions:
            doc_text = f"{q['topic']} {q['title']} {q['description']}".lower()
            doc_tokens = re.findall(r'\w+', doc_text)
            
            score = 0.0
            for token in query_tokens:
                count = doc_tokens.count(token)
                if count > 0:
                    score += (1.0 + math.log(count))
            
            if q['topic'] in query.lower() or query.lower() in q['topic']:
                score += 5.0

            scored_questions.append((score, q))

        scored_questions.sort(key=lambda x: x[0], reverse=True)
        return [q for score, q in scored_questions[:n_results]]

    def generate_question(self, topic: str, difficulty: str = "medium", custom_prompt: str = "") -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
        """Generate a question by adapting existing problems from the DSA database."""
        references = self.retrieve_similar(f"{topic} {custom_prompt}", n_results=5)
        
        if not references:
            # No matching problems - create a generic one
            return self._create_generic_question(topic, difficulty, custom_prompt), []

        # Select best reference(s) and adapt
        primary_ref = references[0]
        adapted = self._adapt_problem(primary_ref, difficulty, custom_prompt, references[1:3])
        
        return self._ensure_canonical(adapted, topic, difficulty), references

    def _adapt_problem(self, ref: Dict[str, Any], target_difficulty: str, custom_prompt: str, 
                       secondary_refs: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Adapt a reference problem to create a new variant."""
        
        ref_difficulty = ref.get('difficulty', 'medium')
        topic = ref['topic']
        
        # Difficulty adjustment factors
        diff_map = {'easy': 1, 'medium': 2, 'hard': 3}
        target_level = diff_map.get(target_difficulty, 2)
        ref_level = diff_map.get(ref_difficulty, 2)
        
        # Build adapted question
        adapted = {
            "question_id": f"ADAPT{random.randint(10000, 99999)}",
            "title": self._generate_title(ref['title'], target_difficulty),
            "topic": topic,
            "level": target_level,
            "level_range": target_difficulty.capitalize(),
            "difficulty": target_difficulty,
            "description": self._adapt_description(ref, target_difficulty, custom_prompt),
            "starter_code": self._adapt_starter_code(ref.get('solution_code', ''), target_difficulty),
            "solution": self._adapt_solution(ref.get('solution_code', ''), target_difficulty),
            "language_id": 71,  # Python 3 — RAG questions target Python for DSA modules
            "time_limit": 2.0,
            "memory_limit_kb": 128000,
            "max_score": 1,
            "is_active": True,
            "is_mandatory": False,
            "allow_multiple_languages": False,
            "test_cases": self._adapt_test_cases(ref.get('test_cases', []), target_difficulty, secondary_refs),
        }
        
        return adapted

    def _generate_title(self, ref_title: str, difficulty: str) -> str:
        """Generate a new title based on reference."""
        # Remove common prefixes
        title = ref_title
        for prefix in ["Optimized ", "Efficient ", "Fast "]:
            if title.startswith(prefix):
                title = title[len(prefix):]
        
        prefixes = {
            'easy': ["Basic ", "Fundamental ", "Introductory "],
            'medium': ["Optimized ", "Efficient ", "Practical "],
            'hard': ["Advanced ", "Complex ", "Challenging "],
        }
        prefix = random.choice(prefixes.get(difficulty, prefixes['medium']))
        return f"{prefix}{title} Variant"

    def _adapt_description(self, ref: Dict[str, Any], difficulty: str, custom_prompt: str) -> str:
        """Adapt the problem description for the target difficulty."""
        base_desc = ref.get('description', '')
        
        # Clean up the description
        base_desc = re.sub(r'\s+', ' ', base_desc).strip()
        
        # Difficulty-specific modifications
        difficulty_notes = {
            'easy': (
                "This is a beginner-friendly problem. Focus on correct implementation "
                "of the core algorithm. Consider edge cases like empty input or single elements."
            ),
            'medium': (
                "This problem requires an efficient approach. Aim for optimal time complexity. "
                "Consider the trade-offs between different algorithmic strategies."
            ),
            'hard': (
                "This is a challenging problem. You may need to combine multiple techniques "
                "or optimize for specific constraints. Think about edge cases and performance."
            ),
        }
        
        note = custom_prompt or difficulty_notes.get(difficulty, difficulty_notes['medium'])
        
        description = f"""### Problem Statement

{base_desc}

#### Input Format
- The first line contains an integer `N` representing the size or count of elements.
- The second line contains `N` space-separated elements or integers.

#### Output Format
- Print the computed answer on a single line.

#### Constraints
- `1 <= N <= 10^5`
- `-10^9 <= element <= 10^9`

#### Notes & Guidance
{note}

**Reference:** This problem is adapted from "{ref['title']}" ({ref['difficulty']})."""

        return description

    def _adapt_starter_code(self, solution_code: str, difficulty: str) -> str:
        """Generate starter code based on reference solution."""
        # Extract function signature if possible
        if solution_code:
            # Try to find a function definition
            func_match = re.search(r'def\s+(\w+)\s*\([^)]*\):', solution_code)
            if func_match:
                func_name = func_match.group(1)
                return f"""#include <stdio.h>
#include <stdlib.h>

// Function to implement: {func_name}
// TODO: Implement the solution

int main(void) {{
    int n;
    if (scanf("%d", &n) != 1) return 0;
    
    // Read input
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {{
        scanf("%d", &arr[i]);
    }}
    
    // Call your function and print result
    // printf("%d\\n", {func_name}(arr, n));
    
    free(arr);
    return 0;
}}"""
        
        return """#include <stdio.h>
#include <stdlib.h>

// TODO: Implement your solution here
// Read N, then N integers, compute and print the result

int main(void) {{
    int n;
    if (scanf("%d", &n) != 1) return 0;
    
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {{
        scanf("%d", &arr[i]);
    }}
    
    // Your algorithm here
    
    free(arr);
    return 0;
}}"""

    def _adapt_solution(self, solution_code: str, difficulty: str) -> str:
        """Adapt the reference solution."""
        if solution_code:
            # Clean up and return as reference
            return f"# Reference solution (adapted from existing problem):\n{solution_code}"
        
        return """def solve():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    
    # TODO: Implement actual algorithm
    print(sum(arr))

if __name__ == '__main__':
    solve()"""

    def _adapt_test_cases(self, original_cases: List[Dict], difficulty: str, 
                          secondary_refs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Create test cases by adapting originals and adding variety."""
        adapted = []
        
        # Use original test cases as base
        for i, tc in enumerate(original_cases[:3]):
            inp = tc.get('input', '').strip()
            exp = tc.get('expected', tc.get('expected_output', '')).strip()
            if inp and exp:
                adapted.append({
                    "input": inp,
                    "expected_output": exp,
                    "is_sample": i == 0
                })
        
        # Add standard test cases if not enough
        standard_cases = [
            ("5\n1 2 3 4 5\n", "15\n"),
            ("3\n10 -2 5\n", "13\n"),
            ("1\n42\n", "42\n"),
            ("4\n0 0 0 0\n", "0\n"),
            ("6\n-1 -2 -3 -4 -5 -6\n", "-21\n"),
        ]
        
        for inp, exp in standard_cases:
            if len(adapted) >= 5:
                break
            if not any(c['input'] == inp for c in adapted):
                adapted.append({
                    "input": inp,
                    "expected_output": exp,
                    "is_sample": len(adapted) == 0
                })
        
        # Add edge cases for harder difficulties
        if difficulty == 'hard' and len(adapted) < 7:
            edge_cases = [
                ("10\n1 1 1 1 1 1 1 1 1 1\n", "10\n"),
                ("5\n-5 -4 -3 -2 -1\n", "-15\n"),
                ("7\n100 200 300 400 500 600 700\n", "2800\n"),
            ]
            for inp, exp in edge_cases:
                if len(adapted) >= 7:
                    break
                if not any(c['input'] == inp for c in adapted):
                    adapted.append({
                        "input": inp,
                        "expected_output": exp,
                        "is_sample": False
                    })
        
        # Ensure first is sample
        if adapted and not adapted[0].get('is_sample'):
            adapted[0]['is_sample'] = True
        
        return adapted[:8]  # Max 8 test cases

    def _create_generic_question(self, topic: str, difficulty: str, custom_prompt: str) -> Dict[str, Any]:
        """Fallback when no references found."""
        diff_map = {'easy': 1, 'medium': 2, 'hard': 3}
        level = diff_map.get(difficulty, 2)
        topic_title = topic.replace('_', ' ').title()
        
        return {
            "question_id": f"GEN{random.randint(10000, 99999)}",
            "title": f"{difficulty.capitalize()} {topic_title} Problem",
            "topic": topic,
            "level": level,
            "level_range": difficulty.capitalize(),
            "difficulty": difficulty,
            "description": f"""### Problem Statement

Implement an algorithm for **{topic_title}** at {difficulty} level.

{custom_prompt or f'Focus on optimal solution using {topic_title} concepts.'}

#### Input Format
- The first line contains an integer `N`
- The second line contains `N` space-separated integers

#### Output Format
- Print the result on a single line

#### Constraints
- `1 <= N <= 10^5`
- `-10^9 <= element <= 10^9`""",
            "starter_code": """#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    
    int *arr = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    // TODO: Implement algorithm
    
    free(arr);
    return 0;
}""",
            "solution": "def solve():\n    import sys\n    input_data = sys.stdin.read().split()\n    if not input_data:\n        return\n    n = int(input_data[0])\n    arr = [int(x) for x in input_data[1:n+1]]\n    print(sum(arr))\n\nif __name__ == '__main__':\n    solve()",
            "time_limit": 2.0,
            "memory_limit_kb": 128000,
            "max_score": 1,
            "is_active": True,
            "is_mandatory": False,
            "allow_multiple_languages": False,
            "language_id": 71,  # Python 3
            "test_cases": [
                {"input": "5\n1 2 3 4 5\n", "expected_output": "15\n", "is_sample": True},
                {"input": "3\n10 -2 5\n", "expected_output": "13\n", "is_sample": False},
                {"input": "1\n42\n", "expected_output": "42\n", "is_sample": False},
            ],
        }

    def _ensure_canonical(self, parsed: Dict[str, Any], topic: str, difficulty: str) -> Dict[str, Any]:
        """Fill missing canonical keys."""
        difficulty = str(difficulty or parsed.get("difficulty") or "medium").lower()
        if difficulty not in {"easy", "medium", "hard"}:
            difficulty = "medium"
        try:
            level = int(parsed.get("level"))
        except (TypeError, ValueError):
            level = {"easy": 1, "medium": 4, "hard": 7}[difficulty]

        test_cases = []
        for idx, tc in enumerate(parsed.get("test_cases") or []):
            if not isinstance(tc, dict):
                continue
            expected = tc.get("expected_output", tc.get("expected", ""))
            if str(expected) == "":
                continue
            test_cases.append({
                "input": str(tc.get("input", "")),
                "expected_output": str(expected),
                "is_sample": bool(tc.get("is_sample", idx == 0)),
            })
        if test_cases and not any(tc["is_sample"] for tc in test_cases):
            test_cases[0]["is_sample"] = True

        return {
            "question_id": str(parsed.get("question_id") or f"ADAPT{random.randint(10000, 99999)}"),
            "title": str(parsed.get("title", "")),
            "topic": str(parsed.get("topic") or topic),
            "level": level,
            "level_range": str(parsed.get("level_range") or difficulty.capitalize()),
            "difficulty": difficulty,
            "description": str(parsed.get("description", "")),
            "starter_code": str(parsed.get("starter_code", "")),
            "solution": str(parsed.get("solution", "")),
            "time_limit": parsed.get("time_limit", 2),
            "memory_limit_kb": parsed.get("memory_limit_kb", 128000),
            "max_score": parsed.get("max_score", 1),
            "is_active": bool(parsed.get("is_active", True)),
            "is_mandatory": bool(parsed.get("is_mandatory", False)),
            "allow_multiple_languages": bool(parsed.get("allow_multiple_languages", False)),
            "language_id": int(parsed.get("language_id") or 71),
            "test_cases": test_cases,
        }