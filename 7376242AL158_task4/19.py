n = int(input("Enter number of readings: "))
lst = []
for _ in range(n):
    line = input("Enter reading as key=value pairs (space-separated): ")
    parts = line.split()
    d = {}
    for p in parts:
        k, v = p.split("=")
        d[k] = v
    lst.append(d)
set1 = set(lst[0].keys())
lst1 = []
for i, r in enumerate(lst):
    if set(r.keys()) != set1:
        lst1.append((i, r))
print("All readings have same keys:", len(lst1) == 0)
print("Faulty readings:", lst1)
