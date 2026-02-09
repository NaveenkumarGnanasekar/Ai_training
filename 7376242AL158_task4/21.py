n = int(input("Enter number of students: "))
dict = {}
for _ in range(n):
    name = input("Student name: ")
    qids = list(map(int, input("Enter question IDs attempted (space-separated): ").split()))
    dict[name] = qids
set1 = set()
for qlist in dict.values():
    set1 |= set(qlist)
print("Total unique questions attempted:", len(set1))
print("Unique question IDs:", set1)
result = []
for student, qlist in dict.items():
    if set(qlist) == set1:
        result.append(student)
print("Students who attempted all questions attempted by others:", result)
