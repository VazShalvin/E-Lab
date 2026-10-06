import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import User, Question, Submission
from core.tasks import evaluate_submission

student = User.objects.get(username="student_test")
question = Question.objects.filter(language_id=62, slug__startswith="generate-resume-interface").first()
sub = Submission.objects.create(
    user=student,
    question=question,
    language_id=62,
    code="""import java.util.Scanner;
interface Resume { void biodata(); }
class Teacher implements Resume {
    String name, qual, exp, ach;
    Teacher(String n, String q, String e, String a) { name=n; qual=q; exp=e; ach=a; }
    public void biodata() { System.out.printf("Teacher Resume:\\nName: %s\\nQualification: %s\\nExperience: %s\\nAchievements: %s\\n", name, qual, exp, ach); }
}
class Student implements Resume {
    String name, res, disc;
    Student(String n, String r, String d) { name=n; res=r; disc=d; }
    public void biodata() { System.out.printf("Student Resume:\\nName: %s\\nResult: %s\\nDiscipline: %s\\n", name, res, disc); }
}
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String type = sc.nextLine().trim();
        if (type.equals("Teacher")) {
            Teacher t = new Teacher(sc.nextLine().trim(), sc.nextLine().trim(), sc.nextLine().trim(), sc.nextLine().trim());
            t.biodata();
        } else {
            Student s = new Student(sc.nextLine().trim(), sc.nextLine().trim(), sc.nextLine().trim());
            s.biodata();
        }
    }
}
"""
)
evaluate_submission(sub.id)
sub.refresh_from_db()
print(f"Status: {sub.status}, Output: {sub.compiler_output}, Error: {sub.error_message}")
