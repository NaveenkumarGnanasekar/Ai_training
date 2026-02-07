n = int(input("enter the number of records: "))
lst = []
for _ in range(n):
    d = {}  
    num = int(input("enter the number of pairs: "))
    for _ in range(num):
        key = input("enter key (string): ")
        value = int(input("enter value (int): "))
        d[key] = value
    lst.append(d)
u = set()
d = []
for i in lst:
    f = frozenset(i.items())
    if f in u:
        d.append(i)
    else:
        u.add(f)
if d:
    print("Duplicate records:")
    for i in d:
        print(i)
else:
    print("No duplicate records")