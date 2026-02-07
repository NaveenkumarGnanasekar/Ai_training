data = [
    {"dept": "HR", "gender": "M"},
    {"dept": "HR", "gender": "F"},
    {"dept": "IT", "gender": "M"},
    {"dept": "Finance", "gender": "M"}
]
s = {
    "rows": len(data),
    "unique_values": {}
}
if not data:
    print(s)
for key in data[0]:
    u = set()
    for row in data:
        if key in row:
            u.add(row[key])
    s["unique_values"][key] = len(u)
print(s)
