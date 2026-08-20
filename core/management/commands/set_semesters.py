from django.core.management.base import BaseCommand
from core.models import User, Module

class Command(BaseCommand):
    help = 'Set semester information for users and modules'

    def handle(self, *args, **options):
        # Set semester for modules based on their names
        self.stdout.write("Setting module semesters...")
        
        # First semester modules
        first_sem_modules = Module.objects.filter(
            name__in=[
                'Basics and IO', 'Operators and Expressions', 
                'Conditionals', 'Loops'
            ]
        )
        first_sem_modules.update(semester=1)
        
        # Second semester modules
        second_sem_modules = Module.objects.filter(
            name__in=[
                'Arrays', 'Strings', 'Functions', 
                'Pointers', 'Structures', 'File Handling', 
                'Advanced Concepts'
            ]
        )
        second_sem_modules.update(semester=2)
        
        # Set user semesters based on their year
        self.stdout.write("Setting user semesters...")
        
        # First year students (semesters 1-2)
        User.objects.filter(email__contains='1rn').update(semester=1)
        User.objects.filter(email__contains='2rn').update(semester=2)
        
        # Second year students (semesters 3-4)
        User.objects.filter(email__contains='3rn').update(semester=3)
        User.objects.filter(email__contains='4rn').update(semester=4)
        
        # Third year students (semesters 5-6)
        User.objects.filter(email__contains='5rn').update(semester=5)
        User.objects.filter(email__contains='6rn').update(semester=6)
        
        # Fourth year students (semesters 7-8)
        User.objects.filter(email__contains='7rn').update(semester=7)
        User.objects.filter(email__contains='8rn').update(semester=8)
        
        self.stdout.write(self.style.SUCCESS('Successfully set semesters'))