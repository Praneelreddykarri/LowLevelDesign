from IceCream import IceCream

class VanillaIceCream(IceCream):
    """Concrete component - Vanilla ice cream."""

    def cost(self) -> float:
        return 50.0  # Base cost of vanilla ice cream

    def description(self) -> str:
        return "Vanilla Ice Cream"
