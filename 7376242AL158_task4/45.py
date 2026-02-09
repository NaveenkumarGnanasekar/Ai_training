n = int(input("Enter number of products: "))
products = []

for _ in range(n):
    pid = input("Product ID: ")
    cat = input("Category: ")
    stock = int(input("Stock: "))
    products.append({"product_id": pid, "category": cat, "stock": stock})

all_stock_positive = all(p["stock"] > 0 for p in products)

out_of_stock_categories = set()
for p in products:
    if p["stock"] == 0:
        out_of_stock_categories.add(p["category"])

print("All products stock > 0:", all_stock_positive)
print("Categories with out-of-stock products:", out_of_stock_categories)