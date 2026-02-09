n = int(input("Enter number of users: "))
usage = {}

for _ in range(n):
    uid = input("User ID: ")
    data = list(map(float, input("Daily data usage list: ").split()))
    usage[uid] = data

limit = float(input("Enter usage limit: "))

exceeded = []
avg_usage = {}

for uid, data in usage.items():
    total = sum(data)
    avg = total / len(data)

    avg_usage[uid] = avg
    if total > limit:
        exceeded.append(uid)

max_user = max(avg_usage, key=avg_usage.get)

print("Users exceeded total limit:", exceeded)
print("User with highest average daily usage:", max_user, "(", avg_usage[max_user], ")")