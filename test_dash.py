import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.test import Client
from core.models import User
u = User.objects.filter(role='student').first()
c = Client()
c.force_login(u)
res = c.get('/dashboard/?course=7')
print(res.status_code)
html = res.content.decode()
import re
title = re.search(r'<h3[^>]*>(.*?)</h3>', html, re.S)
if title: print('Title:', title.group(1).strip())
