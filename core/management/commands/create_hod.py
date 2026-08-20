from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import User

class Command(BaseCommand):
    help = 'Creates a Head of Department (HOD) user'

    def handle(self, *args, **options):
        User = get_user_model()
        
        if User.objects.filter(role=User.Role.HOD).exists():
            self.stdout.write(self.style.WARNING('HOD user already exists'))
            return
            
        # Create HOD user
        hod = User.objects.create_user(
            username='hod',
            password='hodpassword',  # Change this in production!
            first_name='Head',
            last_name='Department',
            email='hod@example.com',
            role=User.Role.HOD,
            is_staff=True
        )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created HOD user: {hod.username}'))
        self.stdout.write(self.style.WARNING('IMPORTANT: Change the default password immediately!'))