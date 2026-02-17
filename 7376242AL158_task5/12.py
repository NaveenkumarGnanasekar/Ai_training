class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def calculate_price(self):
        return self.price
class VegFood(FoodItem):
    def calculate_price(self):
        return self.price + (self.price * 0.05)
class NonVegFood(FoodItem):
    def calculate_price(self):
        return self.price + (self.price * 0.10)
class Beverage(FoodItem):
    def calculate_price(self):
        return self.price + (self.price * 0.02) + 10
item1 = VegFood("Paneer Pizza", 200)
item2 = NonVegFood("Chicken Burger", 150)
item3 = Beverage("Cold Drink", 50)
print(item1.name, ":", item1.calculate_price())
print(item2.name, ":", item2.calculate_price())
print(item3.name, ":", item3.calculate_price())
