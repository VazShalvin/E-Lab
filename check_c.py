import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from core.models import Question
q = Question.objects.filter(module__course__name='C Programming').first()
print(f"ID: {q.id}")
print(f"Language ID: {q.language_id}")
print(f"Allow Multi: {q.allow_multiple_languages}")
print(f"Starter Code: {q.starter_code}")
