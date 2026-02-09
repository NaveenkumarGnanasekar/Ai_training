n = int(input("enter number of students: "))
dict = {}
for _ in range(n):
    name = input("student: ")
    assigns = set(input("assignment IDs submitted (space-separated): ").split())
    dict[name] = assigns
all_assignments = set()
for s in dict.values():
    all_assignments |= s
submitted_all = [st for st, s in dict.items() if s == all_assignments]
not_submitted = set(input("enter total assignment IDs (space-separated): ").split()) - all_assignments
print("students who submitted all assignments:", submitted_all)
print("assignments not submitted by any student:", not_submitted)
