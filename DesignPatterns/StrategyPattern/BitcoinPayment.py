from PaymentStrategy import PaymentStrategy

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float):
        print(f"Processing Bitcoin payment of {amount} using wallet {self.wallet_address}.")
