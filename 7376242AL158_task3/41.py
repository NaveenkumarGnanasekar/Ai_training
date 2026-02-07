lst = [
    {"name": "Alice", "marks": 85, "attendance": 90},
    {"name": "Bob", "marks": 78, "attendance": 95},
    {"name": "Charlie", "marks": 92, "attendance": 80}
]
performance = {}
for i in lst:
    index = i["marks"] * 0.7 + i["attendance"] * 0.3
    performance[i["name"]] = index
topper = max(performance, key=performance.get)
print("Performance Index:", performance)
print("Topper:", topper, "with index", performance[topper])
