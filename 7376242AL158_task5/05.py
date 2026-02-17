class Vehicle:
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    def drive(self):
        print(f"{self.brand} is driving.")

    def display_info(self):
        print(f"Brand: {self.brand} | Fuel: {self.fuel_type}")


class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is cruising on the highway. ")


class Truck(Vehicle):
    def drive(self):
        print(f"{self.brand} truck is hauling heavy cargo. ")


class Motorcycle(Vehicle):
    def drive(self):
        print(f"{self.brand} motorcycle is speeding on the road. ")


class Boat(Vehicle):
    def drive(self):
        print(f"{self.brand} boat is sailing across the water.")


vehicles = [
    Car("Toyota", "Petrol"),
    Truck("Volvo", "Diesel"),
    Motorcycle("Yamaha", "Petrol"),
    Boat("Bayliner", "Diesel"),
]

for v in vehicles:
    v.display_info()
    v.drive()
    print()
