n = int(input("Enter number of students: "))
dict = {}

for _ in range(n):
    name = input("Student: ")
    days = set(input("Days present (space-separated): ").split())
    dict[name] = days

set1 = set(input("Enter all working days (space-separated): ").split())

for name, days in dict.items():
    print(name, "total attendance:", len(days))

present = [name for name, days in dict.items() if days == set1]

print("Students attended all working days:", present)
