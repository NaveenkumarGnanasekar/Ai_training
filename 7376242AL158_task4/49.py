n = int(input("Enter number of orders: "))
orders = []

for _ in range(n):
    oid = input("Order ID: ")
    restaurant = input("Restaurant: ")
    items = input("Items (space-separated): ").split()
    orders.append({"order_id": oid, "restaurant": restaurant, "items": items})


empty_orders = [o["order_id"] for o in orders if len(o["items"]) == 0]


dup_restaurants = set()

for o in orders:
    items = o["items"]
    if len(items) != len(set(items)):  
        dup_restaurants.add(o["restaurant"])

print("Orders with no items:", empty_orders)
print("Restaurants with duplicate items in an order:", dup_restaurants)
