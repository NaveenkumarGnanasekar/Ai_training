class Package:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.status = "Created"
        self.delivery_days = 0

    def ship(self):
        self.status = "Shipped"

    def deliver(self):
        self.status = "Delivered"

    def show_details(self):
        print("Sender:", self.sender)
        print("Receiver:", self.receiver)
        print("Status:", self.status)
        print("Estimated Delivery (days):", self.delivery_days)


class StandardDelivery(Package):
    def ship(self):
        super().ship()
        self.delivery_days = 5



class ExpressDelivery(Package):
    def ship(self):
        super().ship()
        self.delivery_days = 2

class OvernightDelivery(Package):
    def ship(self):
        super().ship()
        self.delivery_days = 1
p1 = StandardDelivery("Alice", "Bob")
p2 = ExpressDelivery("John", "Emma")
p3 = OvernightDelivery("Mike", "Sara")
p1.ship()
p2.ship()
p3.ship()
p1.show_details()
p2.show_details()
p3.show_details()
p1.deliver()
p1.show_details()
