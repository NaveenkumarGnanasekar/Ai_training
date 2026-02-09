n = int(input("Enter number of categories: "))
dict = {}
for _ in range(n):
    category = input("Category: ")
    amounts = list(map(float, input("Enter sale amounts (space-separated): ").split()))
    dict[category] = amounts
dict1 = {}
for cat, amounts in dict.items():
    dict1[cat] = sum(amounts)
max_cat = max(dict1, key=dict1.get)
print("Total sales per category:", dict1)
print("Category with highest total revenue:", max_cat, "(", dict1[max_cat], ")")
