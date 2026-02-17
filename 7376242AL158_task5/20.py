class Ride:
    def __init__(self, pickup, drop, distance):
        self.pickup = pickup
        self.drop = drop
        self.distance = distance

    def calculate_fare(self):
 
        pass

    def ride_details(self):
        print(f"Pickup Location: {self.pickup}")
        print(f"Drop Location: {self.drop}")
        print(f"Distance: {self.distance} km")



class EconomyRide(Ride):
    RATE_PER_KM = 10

    def calculate_fare(self):
        return self.distance * self.RATE_PER_KM



class PremiumRide(Ride):
    RATE_PER_KM = 20
    BASE_CHARGE = 50

    def calculate_fare(self):
        return self.BASE_CHARGE + (self.distance * self.RATE_PER_KM)



class LuxuryRide(Ride):
    RATE_PER_KM = 40
    BASE_CHARGE = 100

    def calculate_fare(self):
        return self.BASE_CHARGE + (self.distance * self.RATE_PER_KM)




pickup = input("Enter Pickup Location: ")
drop = input("Enter Drop Location: ")
distance = float(input("Enter Distance (in km): "))

print("\nSelect Ride Type:")
print("1. Economy")
print("2. Premium")
print("3. Luxury")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    ride = EconomyRide(pickup, drop, distance)
elif choice == 2:
    ride = PremiumRide(pickup, drop, distance)
elif choice == 3:
    ride = LuxuryRide(pickup, drop, distance)
else:
    print("Invalid choice!")
    exit()

print("\n--- Ride Details ---")
ride.ride_details()
print(f"Total Fare: ₹{ride.calculate_fare()}")
