from PaymentStrategy import PaymentStrategy

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Allows changing the strategy at runtime."""
        self._strategy = strategy

    def process_payment(self, amount: float):
        """Process the payment using the current strategy."""
        self._strategy.pay(amount)
