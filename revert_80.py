import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import User, Submission, AssignedQuestion

s = User.objects.get(username='student80')

# Find 7 assigned questions that are completed but NOT mandatory
aqs = AssignedQuestion.objects.filter(
    assignment__student=s, 
    completed_at__isnull=False,
    question__is_mandatory=False
)[:7]

for aq in aqs:
    print("Reverting:", aq.question.title)
    # Remove submissions
    Submission.objects.filter(student=s, question=aq.question).delete()
    # Uncomplete assigned question
    aq.completed_at = None
    aq.save()

print('Submissions left:', Submission.objects.filter(student=s).count())
print('AssignedQs left:', AssignedQuestion.objects.filter(assignment__student=s, completed_at__isnull=False).count())

# Let's also reset the certificate request so the HOD can approve it again
from core.models import CertificateRequest, Certificate
Certificate.objects.filter(student=s).delete()
CertificateRequest.objects.filter(student=s).update(status=CertificateRequest.Status.PENDING_HOD, approved_by_hod=None, hod_notes="")
print("Certificate requests reset.")
