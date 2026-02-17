from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount: float):
        pass

class CreditCard(PaymentMethod):
    def process(self, amount: float):
        return f"Processing ${amount} via Secure Credit Card Gateway."

class PayPal(PaymentMethod):
    def process(self, amount: float):
        return f"Redirecting to PayPal to authorize ${amount} payment."


class Online:
    def __init__(self, order_id, name, amount):
        self.order_id = order_id
        self.name = name 
        self.amount = amount

    def execute_payment(self, method: PaymentMethod, amount: float):
        print(method.process(amount))


order = Online(1, "naveen", 1000)

order.execute_payment(CreditCard(), 1000.0)
order.execute_payment(PayPal(), 1000.0)
