from django.core.management.base import BaseCommand
from django.utils.text import slugify
import json
import logging

from core.models import Module, Question, TestCase, User
from core.rag_agent import RAGQuestionAgent

logger = logging.getLogger(__name__)


def _save_question_to_db(question, module, created_by=None):
    """Persist a canonical-schema question dict into a module."""
    base_slug = slugify(question["title"]) or "question"
    slug = base_slug
    counter = 1
    while Question.objects.filter(module=module, slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    saved = Question.objects.create(
        module=module,
        title=question["title"],
        slug=slug,
        description=question["description"],
        difficulty=question["difficulty"],
        csv_level=question.get("level", 1),
        level_range=question.get("level_range", ""),
        starter_code=question.get("starter_code", ""),
        language_id=int(question.get("language_id") or 71),
        time_limit=float(question.get("time_limit", 2.0)),
        memory_limit_kb=int(question.get("memory_limit_kb", 128000)),
        allow_multiple_languages=bool(question.get("allow_multiple_languages", False)),
        is_mandatory=bool(question.get("is_mandatory", False)),
        is_active=bool(question.get("is_active", True)),
        created_by=created_by,
    )

    test_cases = []
    for idx, tc in enumerate(question.get("test_cases", []), start=1):
        test_cases.append(TestCase.objects.create(
            question=saved,
            stdin=tc.get("input", ""),
            expected_output=tc.get("expected_output", ""),
            is_sample=tc.get("is_sample", idx == 1),
            order=idx,
        ))
    return saved, test_cases


class Command(BaseCommand):
    help = 'Generate a question via problem adaptation (RAG agent) and add it to a module'

    def add_arguments(self, parser):
        parser.add_argument('--topic', type=str, required=True,
                            help='Topic for the question (e.g. "dynamic programming")')
        parser.add_argument('--difficulty', type=str, default='medium',
                            choices=['easy', 'medium', 'hard'])
        parser.add_argument('--prompt', type=str, default='',
                            help='Extra faculty instructions for problem adaptation')
        parser.add_argument('--module', type=str, default='',
                            help='Module name to add the question to')
        parser.add_argument('--module-id', type=int, default=None,
                            help='Module ID to add the question to')
        parser.add_argument('--faculty', type=str, default='',
                            help='Faculty username set as creator')
        parser.add_argument('--output', type=str, default=None,
                            help='Also write the generated JSON to this file')
        parser.add_argument('--dry-run', action='store_true',
                            help='Generate but do not save to the database')

    def handle(self, *args, **options):
        topic = options['topic'].strip()
        difficulty = options['difficulty']
        module_name = options['module']
        module_id = options['module_id']

        if not topic:
            self.stdout.write(self.style.ERROR('Topic is required'))
            return

        if module_id:
            try:
                module = Module.objects.get(pk=module_id)
            except Module.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Module with ID {module_id} not found'))
                return
        elif module_name:
            try:
                module = Module.objects.get(name__iexact=module_name)
            except Module.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Module "{module_name}" not found'))
                return
            except Module.MultipleObjectsReturned:
                self.stdout.write(self.style.ERROR(f'Multiple modules match "{module_name}". Use --module-id.'))
                return
        else:
            self.stdout.write(self.style.WARNING('No module specified. Available modules:'))
            for m in Module.objects.all()[:20]:
                self.stdout.write(f'  ID: {m.pk} - {m.name}')
            self.stdout.write('Use --module "name" or --module-id N')
            return

        faculty = None
        if options['faculty']:
            try:
                faculty = User.objects.get(username=options['faculty'])
            except User.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Faculty "{options["faculty"]}" not found'))
                return

        self.stdout.write(self.style.SUCCESS(f'Generating question for "{topic}" ({difficulty})'))
        self.stdout.write(f'Module: {module.name} (ID: {module.pk})')
        if options['dry_run']:
            self.stdout.write(self.style.WARNING('DRY RUN - will not save to database'))

        try:
            agent = RAGQuestionAgent.get_instance()
            question, references = agent.generate_question(topic, difficulty, options['prompt'])
        except Exception as e:
            logger.exception('Question generation failed')
            self.stdout.write(self.style.ERROR(f'Generation failed: {e}'))
            return

        self.stdout.write(self.style.SUCCESS(f'\n✅ Generated: "{question["title"]}"'))
        self.stdout.write(f'Difficulty: {question["difficulty"]} | Level: {question.get("level")} | '
                          f'Test cases: {len(question.get("test_cases", []))}')
        if references:
            self.stdout.write(f'\n📚 Based on {len(references)} reference questions:')
            for ref in references:
                self.stdout.write(f'   - {ref.get("title", "Unknown")} ({ref.get("difficulty", "unknown")})')

        output = json.dumps(question, indent=2)
        if options['output']:
            with open(options['output'], 'w') as f:
                f.write(output)
            self.stdout.write(f'\n💾 JSON saved to: {options["output"]}')
        else:
            self.stdout.write('\n📄 Generated Question JSON:')
            self.stdout.write(output)

        if not options['dry_run']:
            try:
                saved, test_cases = _save_question_to_db(question, module, created_by=faculty)
                self.stdout.write(self.style.SUCCESS(
                    f'\n✅ Saved to database! Question ID: {saved.pk}, '
                    f'Slug: {saved.slug}, Test cases: {len(test_cases)}'
                ))
            except Exception as e:
                logger.exception('Saving generated question failed')
                self.stdout.write(self.style.ERROR(f'Save failed: {e}'))