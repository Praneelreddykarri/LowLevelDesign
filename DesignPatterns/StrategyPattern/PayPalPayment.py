from PaymentStrategy import PaymentStrategy

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"Processing PayPal payment of {amount} for {self.email}.")
