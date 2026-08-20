import os
import re
import json
import math
import random
import requests
from pathlib import Path
from typing import List, Dict, Any, Tuple
from django.conf import settings

BASE_DIR = getattr(settings, 'BASE_DIR', Path(__file__).resolve().parent.parent)
DSA_TOPICS_DIR = os.path.join(BASE_DIR, 'data', 'DSA_Topics')
OLLAMA_URL = os.environ.get('OLLAMA_URL', 'http://localhost:11434/api/chat')
OLLAMA_MODEL = os.environ.get('OLLAMA_MODEL', 'qwen2.5-coder:3b')


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

    def _parse_markdown_file(self, filepath: Path, topic: str) -> Dict[str, Any]:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
        
        # Extract title
        title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filepath.stem.replace('_', ' ').title()
        
        # Extract description
        desc_match = re.search(r'^#\s+.*?\n(.*?)(?=\n##|\n```)', content, re.DOTALL | re.MULTILINE)
        problem_desc = desc_match.group(1).strip() if desc_match else content[:600]

        # Extract code blocks if any
        code_blocks = re.findall(r'```(?:python|c|cpp|java)?\s*\n(.*?)```', content, re.DOTALL)
        solution_code = "\n\n".join(code_blocks).strip() if code_blocks else ""

        # Extract test cases/examples
        test_cases = []
        tc_matches = re.findall(r'Input:\s*(.*?)\s*Output:\s*(.*?)(?=\n\n|\nInput:|\n##|\Z)', content, re.DOTALL)
        for inp, out in tc_matches:
            test_cases.append({
                "input": inp.strip().replace('*', ''),
                "expected": out.strip().replace('*', '')
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
                        pass

        self.questions = parsed
        RAGQuestionAgent._questions_cache = parsed

    def list_topics(self) -> List[str]:
        topics = sorted(list(set(q["topic"] for q in self.questions)))
        return topics if topics else [
            "array", "string", "linked list", "stack", "queue",
            "binary trees", "binary search", "heap", "hash map",
            "graph bfs dfs", "dynamic programming", "backtracking",
            "greedy", "two pointers", "bit manipulation", "sorting"
        ]

    def retrieve_similar(self, query: str, n_results: int = 3) -> List[Dict[str, Any]]:
        if not self.questions:
            return []

        query_tokens = set(re.findall(r'\w+', query.lower()))
        if not query_tokens:
            return self.questions[:n_results]

        scored_questions = []
        for q in self.questions:
            doc_text = f"{q['topic']} {q['title']} {q['description']} {' '.join(q.get('tags', []))}".lower()
            doc_tokens = re.findall(r'\w+', doc_text)
            
            # Simple TF-IDF / Token Match Scoring
            score = 0.0
            for token in query_tokens:
                count = doc_tokens.count(token)
                if count > 0:
                    score += (1.0 + math.log(count))
            
            # Boost if topic matches directly
            if q['topic'] in query.lower() or query.lower() in q['topic']:
                score += 5.0

            scored_questions.append((score, q))

        scored_questions.sort(key=lambda x: x[0], reverse=True)
        top = [q for score, q in scored_questions[:n_results]]
        return top

    def generate_question(self, topic: str, difficulty: str = "medium", custom_prompt: str = "") -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
        references = self.retrieve_similar(f"{topic} {custom_prompt}", n_results=3)

        context_str = ""
        for i, ref in enumerate(references, 1):
            context_str += f"""
--- Reference Example {i} ---
Title: {ref['title']}
Topic: {ref['topic']}
Difficulty: {ref['difficulty']}
Description: {ref['description'][:500]}
Sample Solution:
{ref['solution_code'][:400]}
"""

        system_prompt = """You are an expert computer science professor and coding assessment creator for a university lab.
Your task: Given a topic and reference questions, generate a high quality ORIGINAL programming problem with test cases.

STRICT JSON OUTPUT REQUIREMENT:
Return ONLY valid JSON matching the canonical E-Lab question schema:
{
  "question_id": "AG001",
  "title": "Short Descriptive Title",
  "topic": "the requested topic",
  "level": 3,
  "level_range": "Easy|Medium|Hard",
  "difficulty": "easy|medium|hard",
  "description": "Comprehensive problem statement including input format, output format, and constraints.",
  "starter_code": "#include <stdio.h>\\n\\nint main() {\\n    // Write your solution here\\n    return 0;\\n}",
  "solution": "# Reference solution (C or Python)",
  "time_limit": 2,
  "memory_limit_kb": 128000,
  "max_score": 1,
  "is_active": true,
  "is_mandatory": false,
  "allow_multiple_languages": false,
  "test_cases": [
    {"input": "2 3\\n", "expected_output": "5\\n", "is_sample": true},
    {"input": "0 0\\n", "expected_output": "0\\n", "is_sample": false}
  ]
}
Rules:
- Provide exactly 5 to 10 test cases; the first one must have is_sample=true (shown to students).
- No duplicate (input, expected_output) pairs.
- difficulty must match the requested difficulty; level ranges from 1 (easiest) to 10 (hardest)."""

        user_prompt = f"""Target Topic: "{topic}"
Requested Difficulty: "{difficulty}"
Faculty Notes/Instructions: "{custom_prompt or 'Create a practical problem suited for lab assessment.'}"

Reference context from question bank:
{context_str}

Generate a brand new original problem. Return ONLY valid raw JSON."""

        # 1. Try Ollama
        try:
            payload = {
                "model": OLLAMA_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "stream": False,
                "format": "json",
                "options": {
                    "temperature": 0.4,
                    "num_ctx": 4096
                }
            }
            res = requests.post(OLLAMA_URL, json=payload, timeout=12)
            if res.status_code == 200:
                raw_json = res.json()["message"]["content"]
                parsed = self._clean_and_parse_json(raw_json)
                if parsed and parsed.get("title") and parsed.get("description"):
                    return self._ensure_canonical(parsed, topic, difficulty), references
        except Exception:
            pass

        # 2. Try Gemini or OpenAI API if configured
        api_result = self._try_external_api(system_prompt, user_prompt)
        if api_result and api_result.get("title") and api_result.get("description"):
            return self._ensure_canonical(api_result, topic, difficulty), references

        # 3. Fallback Smart Synthesis Engine
        fallback_data = self._generate_fallback(topic, difficulty, custom_prompt, references)
        return self._ensure_canonical(fallback_data, topic, difficulty), references

    def _ensure_canonical(self, parsed: Dict[str, Any], topic: str, difficulty: str) -> Dict[str, Any]:
        """Fill any missing canonical-schema keys so agent output always matches the
        training-data format (docs/QUESTION_JSON_SCHEMA.md)."""
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
            "question_id": str(parsed.get("question_id") or f"AG{random.randint(10000, 99999)}"),
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
            "test_cases": test_cases,
        }

    def _clean_and_parse_json(self, raw: str) -> Dict[str, Any]:
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            cleaned = raw.strip()
            if "```" in cleaned:
                blocks = re.findall(r'```(?:json)?\s*\n?(.*?)```', cleaned, re.DOTALL)
                if blocks:
                    cleaned = blocks[0].strip()
            return json.loads(cleaned)

    def _try_external_api(self, system_prompt: str, user_prompt: str) -> Dict[str, Any] | None:
        gemini_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if gemini_key:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={gemini_key}"
                payload = {
                    "contents": [{
                        "parts": [{"text": f"{system_prompt}\n\n{user_prompt}"}]
                    }],
                    "generationConfig": {"response_mime_type": "application/json"}
                }
                res = requests.post(url, json=payload, timeout=15)
                if res.status_code == 200:
                    text = res.json()["candidates"][0]["content"]["parts"][0]["text"]
                    return self._clean_and_parse_json(text)
            except Exception:
                pass

        openai_key = os.environ.get("OPENAI_API_KEY")
        if openai_key:
            try:
                url = "https://api.openai.com/v1/chat/completions"
                headers = {"Authorization": f"Bearer {openai_key}", "Content-Type": "application/json"}
                payload = {
                    "model": "gpt-3.5-turbo",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "response_format": {"type": "json_object"}
                }
                res = requests.post(url, headers=headers, json=payload, timeout=15)
                if res.status_code == 200:
                    text = res.json()["choices"][0]["message"]["content"]
                    return self._clean_and_parse_json(text)
            except Exception:
                pass

        return None

    def _generate_fallback(self, topic: str, difficulty: str, custom_prompt: str, references: List[Dict[str, Any]]) -> Dict[str, Any]:
        ref_title = references[0]['title'] if references else topic.title()
        ref_desc = references[0]['description'] if references else ""
        
        topic_title = topic.replace('_', ' ').title()
        
        title = f"Optimized {topic_title} Algorithm ({ref_title})"
        
        description = f"""### Problem Statement

Given a set of input parameters relevant to **{topic_title}**, write an efficient program to compute the required output according to the problem requirements.

#### Input Format
- The first line contains an integer `N` representing the size or count of elements.
- The second line contains `N` space-separated elements or integers.

#### Output Format
- Print the computed answer on a single line.

#### Constraints
- `1 <= N <= 10^5`
- `-10^4 <= element <= 10^4`

#### Notes & Guidance
{custom_prompt or f'Focus on optimal solution using {topic_title} concepts.'}
"""

        starter_code = """#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;
    
    // Write your code here
    
    return 0;
}"""

        solution = f"""def solve():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    print(sum(arr))

if __name__ == '__main__':
    solve()
"""

        test_cases = [
            {"input": "5\n1 2 3 4 5\n", "expected_output": "15\n", "is_sample": True},
            {"input": "3\n10 -2 5\n", "expected_output": "13\n", "is_sample": False},
            {"input": "1\n42\n", "expected_output": "42\n", "is_sample": False},
            {"input": "4\n0 0 0 0\n", "expected_output": "0\n", "is_sample": False},
            {"input": "6\n-1 -2 -3 -4 -5 -6\n", "expected_output": "-21\n", "is_sample": False},
        ]

        return {
            "question_id": f"AG{random.randint(10000, 99999)}",
            "title": title,
            "topic": topic,
            "level": {"easy": 1, "medium": 4, "hard": 7}[difficulty.lower()],
            "level_range": difficulty.capitalize(),
            "difficulty": difficulty.lower(),
            "description": description,
            "starter_code": starter_code,
            "solution": solution,
            "time_limit": 2,
            "memory_limit_kb": 128000,
            "max_score": 1,
            "is_active": True,
            "is_mandatory": False,
            "allow_multiple_languages": False,
            "test_cases": test_cases,
        }
