import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.test import RequestFactory
from core.views import question_detail
from core.models import User
factory = RequestFactory()
request = factory.get('/questions/2699/')
request.user = User.objects.filter(role='student').first()
# Mock session and messages
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
middleware = SessionMiddleware(lambda r: None)
middleware.process_request(request)
request.session.save()
msg_middleware = MessageMiddleware(lambda r: None)
msg_middleware.process_request(request)

try:
    response = question_detail(request, 2699)
    print(response.status_code)
except Exception as e:
    import traceback
    traceback.print_exc()
