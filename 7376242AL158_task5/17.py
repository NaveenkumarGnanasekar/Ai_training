class UtilityBill:
    def __init__(self, customer_name, customer_id, units):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.units = units
    def calculate_bill(self):
        pass
    def display_bill(self):
        print("Customer Name:", self.customer_name)
        print("Customer ID:", self.customer_id)
        print("Units Consumed:", self.units)
        print("Total Bill Amount: ₹", self.calculate_bill())
class ElectricityBill(UtilityBill):
    def calculate_bill(self):
        rate_per_unit = 5
        return self.units * rate_per_unit
class WaterBill(UtilityBill):
    def calculate_bill(self):
        rate_per_unit = 2
        return self.units * rate_per_unit
class GasBill(UtilityBill):
    def calculate_bill(self):
        rate_per_unit = 8
        return self.units * rate_per_unit
electricity = ElectricityBill("Rahul", 101, 120)
water = WaterBill("Amit", 102, 80)
gas = GasBill("Sneha", 103, 40)
electricity.display_bill()
water.display_bill()
gas.display_bill()
