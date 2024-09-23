from abc import ABC, abstractmethod


class IceCream(ABC):
    """Abstract base class for all ice cream types."""

    @abstractmethod
    def cost(self) -> float:
        """Returns the cost of the ice cream."""
        pass

    @abstractmethod
    def description(self) -> str:
        """Returns the description of the ice cream."""
        pass
