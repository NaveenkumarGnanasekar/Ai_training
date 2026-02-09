n = int(input("enter number of courses: "))
courses = {}
for _ in range(n):
    course = input("course name: ")
    students = set(input("student IDs (space-separated): ").split())
    courses[course] = students
student_count = {}
for st_set in courses.values():
    for st in st_set:
        student_count[st] = student_count.get(st, 0) + 1
multi_course_students = [st for st, c in student_count.items() if c > 1]
max_enroll = max(len(s) for s in courses.values())
max_courses = [c for c, s in courses.items() if len(s) == max_enroll]
print("students in more than one course:", multi_course_students)
print("courses with maximum enrollment:", max_courses, "(", max_enroll, ")")
