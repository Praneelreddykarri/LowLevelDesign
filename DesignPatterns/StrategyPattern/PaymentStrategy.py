from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """The common interface for all payment strategies."""

    @abstractmethod
    def pay(self, amount: float):
        """Method to process the payment."""
        pass
