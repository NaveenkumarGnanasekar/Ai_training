class PaymentSource:
    def pay(self, amount):
        pass 
class CreditCard(PaymentSource):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card.")
class DebitCard(PaymentSource):
    def pay(self, amount):
        print("Paid", amount, "using Debit Card.")
class UPI(PaymentSource):
    def pay(self, amount):
        print("Paid", amount, "using UPI.")
class DigitalWallet:
    def __init__(self):
        self.payment_methods = []

    def add_payment_method(self, method):
        self.payment_methods.append(method)

    def make_payment(self, method, amount):
        method.pay(amount)
wallet = DigitalWallet()

cc = CreditCard()
dc = DebitCard()
upi = UPI()

wallet.add_payment_method(cc)
wallet.add_payment_method(dc)
wallet.add_payment_method(upi)

wallet.make_payment(cc, 1000)
wallet.make_payment(dc, 500)
wallet.make_payment(upi, 200)
