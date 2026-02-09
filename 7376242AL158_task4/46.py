n = int(input("Enter number of employees: "))
certs = {}

for _ in range(n):
    emp = input("Employee: ")
    c = set(input("Certifications (space-separated): ").split())
    certs[emp] = c


common = None
for c in certs.values():
    if common is None:
        common = c.copy()
    else:
        common &= c


all_certs = {}
for emp, c in certs.items():
    for cert in c:
        all_certs[cert] = all_certs.get(cert, 0) + 1

unique_emps = []
for emp, c in certs.items():
    if any(all_certs[cert] == 1 for cert in c):
        unique_emps.append(emp)

print("Certifications held by all employees:", common)
print("Employees with unique certifications:", unique_emps)
