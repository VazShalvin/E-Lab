from core.models import Question, Course, Module
for c in Course.objects.all():
    print(c.name)
