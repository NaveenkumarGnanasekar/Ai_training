n = int(input("Enter number of students: "))
progress = {}

for _ in range(n):
    name = input("Student: ")
    lessons = set(input("Completed lessons (space-separated): ").split())
    progress[name] = lessons

all_lessons = set(input("Enter all lesson IDs (space-separated): ").split())

completed_all = [st for st, s in progress.items() if s == all_lessons]

less_than_half = []
half = len(all_lessons) / 2

for st, s in progress.items():
    if len(s) < half:
        less_than_half.append(st)

print("Students completed all lessons:", completed_all)
print("Students completed less than half:", less_than_half)
