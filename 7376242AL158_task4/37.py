n = int(input("Enter number of students: "))
dict = {}

for _ in range(n):
    st = input("Student name: ")
    chosen = set(input("Preferred teammates (space-separated): ").split())
    dict[st] = chosen
mutual = []

students = list(dict.keys())
for a in students:
    for b in dict[a]:
        if b in dict and a in dict[b]:
            pair = tuple(sorted((a, b)))
            if pair not in mutual:
                mutual.append(pair)
chosen_by_anyone = set()
for chosen in dict.values():
    chosen_by_anyone |= chosen

isolated = [st for st in dict if st not in chosen_by_anyone]

print("Mutual preferences:", mutual)
print("Isolated students:", isolated)
