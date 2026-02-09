n = int(input("enter number of junctions: "))
lst = []
for i in range(n):
    row = list(map(int, input(f"enter hourly vehicle counts for junction {i+1}: ").split()))
    lst.append(row)
totals = [sum(row) for row in lst]
max_junction = totals.index(max(totals)) + 1
hours = len(lst[0])
total = [0] * hours
for row in lst:
    for h in range(hours):
        total[h] += row[h]
max = total.index(max(total)) + 1
print("junction with highest total traffic:", max_junction)
print("hour with highest traffic overall:", max)
