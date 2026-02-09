n = int(input("Enter number of visit records: "))
lst = []
for _ in range(n):
    pid = input("Patient ID: ")
    doctor = input("Doctor: ")
    visits = int(input("Visit count: "))
    lst.append({"patient_id": pid, "doctor": doctor, "visit_count": visits})
dict = {}
max = None
max_v = -1
for r in lst:
    doc = r["doctor"]
    dict[doc] = dict.get(doc, 0) + r["visit_count"]
    if r["visit_count"] > max_v:
        max_v = r["visit_count"]
        max = r["patient_id"]
print("Doctor-wise total visits:", dict)
print("Patient with highest visit count:", max, "(", max_v, ")")
