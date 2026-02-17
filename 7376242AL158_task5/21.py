class SubscriptionPlan:
    def __init__(self, user_name):
        self.user_name = user_name
        self.start_date = "2026-02-17" 
    def calculate_bill(self):
        return 0  
    def plan_details(self):
        print(f"User: {self.user_name}")
        print(f"Start Date: {self.start_date}")
        print(f"Total Bill: ₹{self.calculate_bill()}")
class BasicPlan(SubscriptionPlan):
    def calculate_bill(self):
        return 199  
class PremiumPlan(SubscriptionPlan):
    def calculate_bill(self):
        return 499 
class AnnualPlan(SubscriptionPlan):
    def calculate_bill(self):
        return 4999 

user_name = input("Enter User Name: ")

print("\nSelect Plan:")
print("1. Basic")
print("2. Premium")
print("3. Annual")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    plan = BasicPlan(user_name)
elif choice == 2:
    plan = PremiumPlan(user_name)
elif choice == 3:
    plan = AnnualPlan(user_name)
else:
    print("Invalid choice!")
    exit()

plan.plan_details()  # Display subscription details
