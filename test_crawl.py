import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.test import Client
from core.models import User, Course, Module, Question

u = User.objects.filter(role='student').first()
c = Client()
c.force_login(u)

urls_to_test = [
    '/dashboard/',
    '/overview/',
    '/course-selection/',
]

for course in Course.objects.all():
    urls_to_test.append(f'/dashboard/?course={course.id}')

for module in Module.objects.filter(is_active=True)[:5]:
    urls_to_test.append(f'/modules/{module.id}/')
    urls_to_test.append(f'/modules/{module.id}/easy/')
    urls_to_test.append(f'/modules/{module.id}/medium/')

for q in Question.objects.filter(is_active=True)[:5]:
    urls_to_test.append(f'/questions/{q.id}/')

for url in urls_to_test:
    res = c.get(url)
    if res.status_code >= 400:
        print(f'Error {res.status_code} on {url}')
print("Crawl complete!")
