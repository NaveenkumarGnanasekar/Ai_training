n = int(input("Enter the number of stops: "))
lst = []
for i in range(1, n + 1):
    num = int(input(f"Enter number of passengers at stop {i}: "))
    lst.append(num)
avg = sum(lst) / n
max_passengers = max(lst)
max_stop = lst.index(max_passengers) + 1
sto = []
for index, passengers in enumerate(lst, start=1):
    if passengers > avg:
        sto.append(index)
print(f"The stop with maximum number of passengers = {max_stop}")
print(f"Stops with passengers more than average = {sto}")
