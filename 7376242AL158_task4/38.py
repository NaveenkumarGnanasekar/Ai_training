n = int(input("Enter number of flights: "))
lst = {}
for _ in range(n):
    fid = input("Flight ID: ")
    mins = list(map(int, input("Delay minutes list: ").split()))
    lst[fid] = mins
avg_delay = {}
for fid, mins in lst.items():
    avg_delay[fid] = sum(mins) / len(mins)
worst_flight = max(avg_delay, key=avg_delay.get)
print("Average delay per flight:", avg_delay)
print("Flight with highest average delay:", worst_flight, "(", avg_delay[worst_flight], ")")
