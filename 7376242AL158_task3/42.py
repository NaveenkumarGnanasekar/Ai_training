lst = [
    {"name": "Alice", "marks": 85, "department": "cse"},
    {"name": "Bob", "marks": 92, "department": "aiml"},
    {"name": "Charlie", "marks": 78, "department": "cse"},
    {"name": "David", "marks": 90, "department": "aiml"},
    {"name": "Eve", "marks": 88, "department": "cse"}
]
dict = {}
for i in lst:
    d = i["department"]
    if d not in dict or dict[d]["marks"] < i["marks"]:
        dict[d] = i
for d, topper in dict.items():
    print(f"topper in {d} department: {topper['name']} with {topper['marks']} marks")
