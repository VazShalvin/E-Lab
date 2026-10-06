import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.test import RequestFactory
from core.views import module_level_detail
from core.models import User
u = User.objects.filter(role='student').first()
factory = RequestFactory()
request = factory.get('/modules/121/easy/')
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
    response = module_level_detail(request, 121, 'easy')
    if response.status_code == 200:
        print("200 OK - No 500 Error in Python!")
    else:
        print(f"Status: {response.status_code}")
except Exception as e:
    import traceback
    traceback.print_exc()
