"""
Bulk generate questions from a list of topics.
Usage:
  python manage.py bulk_generate_questions --topics "sorting,linked lists,dynamic programming" --difficulty medium --module-id 1
  python manage.py bulk_generate_questions --file topics.txt --difficulty medium --module-id 1
  python manage.py bulk_generate_questions --topics "sorting" --difficulty easy --module-id 1 --dry-run
"""

import json
from django.core.management.base import BaseCommand, CommandError
from core.rag_agent import RAGQuestionAgent
from core.models import Module, Question, TestCase


class Command(BaseCommand):
    help = "Generate multiple questions from a list of topics and add them to a module."

    def add_arguments(self, parser):
        parser.add_argument(
            "--topics",
            type=str,
            help="Comma-separated list of topics (e.g., 'sorting,linked lists,trees')",
        )
        parser.add_argument(
            "--file",
            type=str,
            help="Path to a text file with one topic per line",
        )
        parser.add_argument(
            "--difficulty",
            type=str,
            choices=["easy", "medium", "hard"],
            default="medium",
            help="Difficulty level for all questions",
        )
        parser.add_argument(
            "--module",
            type=str,
            help="Module name to add questions to",
        )
        parser.add_argument(
            "--module-id",
            type=int,
            help="Module ID to add questions to",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Generate but do not save to database",
        )
        parser.add_argument(
            "--output",
            type=str,
            help="Write generated questions JSON to this file",
        )

    def handle(self, *args, **options):
        topics_input = options["topics"]
        file_path = options["file"]
        difficulty = options["difficulty"]
        module_name = options["module"]
        module_id = options["module_id"]
        dry_run = options["dry_run"]
        output_file = options["output"]

        # Collect topics
        topics = []
        if topics_input:
            topics.extend([t.strip() for t in topics_input.split(",") if t.strip()])
        if file_path:
            try:
                with open(file_path, "r") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):
                            topics.append(line)
            except FileNotFoundError:
                raise CommandError(f"File not found: {file_path}")

        if not topics:
            raise CommandError("No topics provided. Use --topics or --file.")

        # Get module
        if module_id:
            try:
                module = Module.objects.get(id=module_id)
            except Module.DoesNotExist:
                raise CommandError(f"Module with ID {module_id} not found")
        elif module_name:
            try:
                module = Module.objects.get(name__iexact=module_name)
            except Module.DoesNotExist:
                raise CommandError(f"Module '{module_name}' not found")
        else:
            raise CommandError("Must specify --module or --module-id")

        agent = RAGQuestionAgent()
        generated_questions = []

        self.stdout.write(f"Generating {len(topics)} questions for module '{module.name}' (difficulty: {difficulty})")

        for i, topic in enumerate(topics, 1):
            self.stdout.write(f"\n[{i}/{len(topics)}] Topic: {topic} ({difficulty})")

            try:
                result, refs = agent.generate_question(topic, difficulty)

                # Save to database if not dry run
                if not dry_run:
                    # Build slug from title
                    from django.utils.text import slugify
                    base_slug = slugify(result["title"])[:160]
                    slug = base_slug
                    counter = 1
                    while Question.objects.filter(module=module, slug=slug).exists():
                        counter += 1
                        slug = f"{base_slug}-{counter}"

                    # Determine language based on module category
                    lang_id = 50  # C default
                    if module.category == "python_programming":
                        lang_id = 71
                    elif module.category in ("placement_training", "advanced_placement_training"):
                        lang_id = 71
                    elif module.category in ("cpp_programming", "c_programming_advanced"):
                        lang_id = 54
                    elif module.category == "java_programming":
                        lang_id = 62

                    question = Question.objects.create(
                        module=module,
                        title=result["title"],
                        slug=slug,
                        description=result["description"],
                        starter_code=result.get("starter_code", ""),
                        difficulty=result["difficulty"],
                        csv_level=result.get("level", 1),
                        level_range=result.get("level_range", difficulty.capitalize()),
                        time_limit=result.get("time_limit", 2),
                        memory_limit_kb=result.get("memory_limit_kb", 128000),
                        allow_multiple_languages=result.get("allow_multiple_languages", False),
                        is_mandatory=result.get("is_mandatory", False),
                        is_active=result.get("is_active", True),
                        language_id=lang_id,
                    )

                    # Create test cases
                    for idx, tc in enumerate(result.get("test_cases", []), 1):
                        TestCase.objects.create(
                            question=question,
                            stdin=tc.get("input", ""),
                            expected_output=tc.get("expected_output", ""),
                            is_sample=tc.get("is_sample", idx == 1),
                            order=idx,
                        )

                    self.stdout.write(self.style.SUCCESS(f"  ✅ Saved: {question.id} - {question.title}"))

                generated_questions.append({
                    "topic": topic,
                    "difficulty": difficulty,
                    "result": result,
                    "saved": not dry_run,
                })

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  ❌ Failed: {e}"))
                generated_questions.append({
                    "topic": topic,
                    "difficulty": difficulty,
                    "error": str(e),
                })

        # Summary
        saved_count = sum(1 for q in generated_questions if q.get("saved"))
        self.stdout.write(f"\n{'='*50}")
        self.stdout.write(f"Generated: {len(generated_questions)} | Saved: {saved_count} | Dry run: {dry_run}")

        if output_file:
            with open(output_file, "w") as f:
                json.dump(generated_questions, f, indent=2)
            self.stdout.write(f"Output written to {output_file}")