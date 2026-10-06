import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.test import RequestFactory
from core.views import question_detail
from core.models import User, Question
# Find a user who has access
q = Question.objects.get(id=2699)
course = q.module.course
u = User.objects.filter(role='student', semester__gte=course.available_from_semester).first()
if not u:
    u = User.objects.filter(role='student').first()
    u.semester = course.available_from_semester
    u.save()

factory = RequestFactory()
request = factory.get(f'/questions/{q.id}/')
request.user = u
# Mock session and messages
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
middleware = SessionMiddleware(lambda r: None)
middleware.process_request(request)
request.session.save()
msg_middleware = MessageMiddleware(lambda r: None)
msg_middleware.process_request(request)

try:
    response = question_detail(request, q.id)
    if response.status_code == 200:
        print("200 OK - No 500 Error in Python!")
    else:
        print(f"Status: {response.status_code}")
except Exception as e:
    import traceback
    traceback.print_exc()
