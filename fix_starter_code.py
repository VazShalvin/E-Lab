import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from core.models import Question

JAVA_STARTER = """import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        // Write your code here
        
    }
}"""

PYTHON_STARTER = """# Write your code here
def solve():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    # Implement your algorithm here

if __name__ == '__main__':
    solve()"""

CPP_STARTER = """#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    if (!(cin >> n)) return 0;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    // Write your code here
    
    return 0;
}"""

updated = 0
for q in Question.objects.all():
    if q.slug.startswith("generate-resume-interface") or q.slug.startswith("n-student-objects") or q.slug.startswith("staff-inheritance") or q.slug.startswith("multilevel-inheritance") or q.slug.startswith("even-and-odd-threads") or q.slug.startswith("thread-synchronization") or q.slug.startswith("arraylist-and-linkedlist") or q.slug.startswith("count-chars-words-lines"):
        continue
    
    if q.language_id == 62 and "#include" in q.starter_code:
        q.starter_code = JAVA_STARTER
        q.save(update_fields=['starter_code'])
        updated += 1
    elif q.language_id == 71 and "#include" in q.starter_code:
        q.starter_code = PYTHON_STARTER
        q.save(update_fields=['starter_code'])
        updated += 1
    elif q.language_id == 54 and "<stdio.h>" in q.starter_code:
        q.starter_code = CPP_STARTER
        q.save(update_fields=['starter_code'])
        updated += 1

print(f"Updated {updated} questions")
