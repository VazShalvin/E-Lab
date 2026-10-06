import os
import django
import random
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import User, Course, Module, Question, Submission, AssignedQuestion, ModuleQuestionAssignment
from core.services import get_or_create_module_assignment

student, _ = User.objects.get_or_create(username='student80', defaults={
    'email': 'student80@example.com', 
    'role': User.Role.STUDENT, 
    'year': 1, 
    'semester': 1, 
    'department': 'CSE'
})
student.set_password('testpass123')
student.save()

modules = Module.objects.filter(is_active=True, category="c_programming")
total_questions_needed = int(modules.count() * 15 * 0.85)

questions_completed = 0
for module in modules:
    for difficulty in [Question.Difficulty.EASY, Question.Difficulty.MEDIUM, Question.Difficulty.HARD]:
        get_or_create_module_assignment(student, module, difficulty)
    
    assignments = ModuleQuestionAssignment.objects.filter(student=student, module=module)
    for assignment in assignments:
        assigned_qs = list(AssignedQuestion.objects.filter(assignment=assignment))
        
        for idx, aq in enumerate(assigned_qs):
            if questions_completed < total_questions_needed:
                aq.unlocked_at = timezone.now()
                aq.completed_at = timezone.now()
                aq.save()
                
                Submission.objects.create(
                    student=student,
                    question=aq.question,
                    code="int main() { return 0; }",
                    status=Submission.Status.ACCEPTED,
                    score=100
                )
                questions_completed += 1
            else:
                aq.unlocked_at = timezone.now() if idx == 0 else None
                aq.save()

print(f"Done. User student80 created with {questions_completed} accepted submissions.")
