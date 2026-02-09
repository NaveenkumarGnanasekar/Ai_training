n = int(input("Enter number of students: "))
lst = []
for _ in range(n):
    name = input("Name: ")
    dept = input("Department: ")
    cgpa = float(input("CGPA: "))
    lst.append({"name": name, "dept": dept, "cgpa": cgpa})
sum = {}
count = {}
for r in lst:
    d = r["dept"]
    sum[d] = sum.get(d, 0) + r["cgpa"]
    count[d] = count.get(d, 0) + 1

summary = {d: sum[d] / count[d] for d in sum}
print("Department average CGPA:", summary)
