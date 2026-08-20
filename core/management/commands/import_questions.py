from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Import questions from CSV files'

    def add_arguments(self, parser):
        parser.add_argument(
            '--second-year',
            action='store_true',
            help='Import second year questions instead of first year'
        )
        parser.add_argument(
            '--third-year',
            action='store_true',
            help='Import third year questions'
        )

    def handle(self, *args, **options):
        if options['third_year']:
            self.stdout.write(self.style.SUCCESS('Importing third year questions...'))
            from scripts.import_third_year import import_third_year_questions
            import_third_year_questions()
        elif options['second_year']:
            self.stdout.write(self.style.SUCCESS('Importing second year questions...'))
            # Call the second year import script
            from scripts.import_second_year import import_second_year_questions
            import_second_year_questions()
        else:
            self.stdout.write(self.style.SUCCESS('Importing first year questions...'))
            # Call the existing import script
            try:
                from scripts.verify_and_import import main
                main()
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error importing questions: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS('Questions import completed'))