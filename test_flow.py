import django
django.setup()
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
client = Client()
client.login(username='teststudent3', password='testpass')
r1 = client.get('/course-selection/')
content = r1.content.decode('utf-8')
import re
links = re.findall(r'<a href="(/dashboard/\?course=\d+|\?course=\d+|/\?course=\d+)"[^>]*>.*?<span>Enter (.*?)</span>', content, re.DOTALL)
print("Course links found:")
for link in links:
    print(link)
