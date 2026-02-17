class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Reservation:
    def __init__(self, customer, time_slot):
        self.customer = customer
        self.time_slot = time_slot


class ReservationPolicy:
    def can_book(self, restaurant, time_slot):
        pass

class NormalPolicy(ReservationPolicy):

    def can_book(self, restaurant, time_slot):
        return time_slot not in restaurant.bookings
class VIPPolicy(ReservationPolicy):
 
    def can_book(self, restaurant, time_slot):
        return True
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.bookings = {} 

    def reserve_table(self, customer, time_slot, policy):
        if policy.can_book(self, time_slot):
            reservation = Reservation(customer, time_slot)
            self.bookings[time_slot] = reservation
            print(f"Reservation confirmed for {customer.name} at {time_slot}")
        else:
            print(f"Sorry {customer.name}, slot {time_slot} is already booked.")
restaurant = Restaurant("Food Palace")
customer1 = Customer("naveen", "12345")
customer2 = Customer("ravi", "67890")
normal_policy = NormalPolicy()
vip_policy = VIPPolicy()
restaurant.reserve_table(customer1, "7 PM", normal_policy)
restaurant.reserve_table(customer2, "7 PM", normal_policy)
restaurant.reserve_table(customer2, "7 PM", vip_policy)
