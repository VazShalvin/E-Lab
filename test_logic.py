def mock_dashboard(course_id, category=None):
    if course_id is None and category is None:
        category = "session_cat"
        course_id = "session_course"
    else:
        pass # update session

    if course_id and not category:
        try:
            course_id_int = int(course_id)
            if course_id_int == 2: # C programming
                category = "c_programming"
            elif course_id_int == 4: # Java
                category = "java_programming"
        except ValueError:
            pass

    if not category:
        category = "advanced_placement_training"
    
    return category

print("Test course=2, category=None:", mock_dashboard("2", None))
print("Test course=4, category=None:", mock_dashboard("4", None))
