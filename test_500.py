import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.test import Client
from core.models import User, Question
u = User.objects.filter(is_superuser=True).first()
q = Question.objects.get(id=2699)
c = Client()
c.force_login(u)
try:
    response = c.get(f'/questions/{q.id}/')
    if response.status_code == 500:
        print("Got 500!")
    else:
        print(f"Status: {response.status_code}")
except Exception as e:
    import traceback
    traceback.print_exc()
