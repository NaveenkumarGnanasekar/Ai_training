n = int(input("enter number of deliveries: "))
deliveries = []
for _ in range(n):
    pid = input("partner ID: ")
    earning = float(input("earning: "))
    deliveries.append((pid, earning))
total = {}
count = {}
for pid, earn in deliveries:
    total[pid] = total.get(pid, 0) + earn
    count[pid] = count.get(pid, 0) + 1
avg = {pid: total[pid] / count[pid] for pid in total}
best_partner = max(avg, key=avg.get)
print("total earning per partner:", total)
print("average earning per delivery:", avg)
print("partner with highest average earning:", best_partner, "(", avg[best_partner], ")")
