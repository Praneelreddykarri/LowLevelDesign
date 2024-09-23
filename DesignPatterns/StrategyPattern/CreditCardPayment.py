from PaymentStrategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float):
        print(f"Processing credit card payment of {amount} using card {self.card_number}.")
