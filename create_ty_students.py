from django.contrib.auth import get_user_model
User = get_user_model()

print("Creating 5 Third Year (TY) student accounts...")

for i in range(1, 6):
    username = f"student_ty_{i:02d}"
    email = f"{username}@nitte.edu.in"
    password = "password123"
    user, created = User.objects.get_or_create(username=username, defaults={
        "email": email,
        "first_name": "Third Year",
        "last_name": f"Student {i}",
        "role": User.Role.STUDENT,
        "semester": 5  # 5th semester
    })
    
    if created:
        user.set_password(password)
        user.save()
        print(f"Created: {username} (Password: {password})")
    else:
        # Just ensure password and semester are correct
        user.semester = 5
        user.set_password(password)
        user.save()
        print(f"Updated: {username} (Password: {password})")

print("Done.")
