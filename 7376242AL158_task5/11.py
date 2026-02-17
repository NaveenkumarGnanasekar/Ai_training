class Transport:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def calculate_fare(self, distance):
        pass 
class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 5
class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 3
class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 10
bus = Bus("City A", "City B")
train = Train("City A", "City B")
flight = Flight("City A", "City B")
distance = 100
print("Bus Fare:", bus.calculate_fare(distance))
print("Train Fare:", train.calculate_fare(distance))
print("Flight Fare:", flight.calculate_fare(distance))
