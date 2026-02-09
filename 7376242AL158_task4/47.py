n = int(input("Enter number of devices: "))
usage = {}

for _ in range(n):
    device = input("Device ID: ")
    hours = list(map(float, input("Usage hours list: ").split()))
    usage[device] = hours

total_usage = {d: sum(h) for d, h in usage.items()}

avg_all = sum(total_usage.values()) / len(total_usage)

above_avg_devices = [d for d, t in total_usage.items() if t > avg_all]

print("Total usage per device:", total_usage)
print("Devices above average usage:", above_avg_devices)