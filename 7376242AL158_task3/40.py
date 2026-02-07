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
base_keys = set(lst[0].keys())
for d in lst:
    if set(d.keys()) != base_keys:
        print("dictionaries do NOT have the same set of keys")
        break
else:
    print("all dictionaries in the list have the same set of keys")
