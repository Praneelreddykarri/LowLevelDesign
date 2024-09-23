from IceCream import IceCream


class ToppingDecorator(IceCream):
    """Base decorator for ice cream toppings."""

    def __init__(self, ice_cream: IceCream):
        self._ice_cream = ice_cream

    def cost(self) -> float:
        return self._ice_cream.cost()

    def description(self) -> str:
        return self._ice_cream.description()


# Chocolate Syrup topping
class ChocolateSyrup(ToppingDecorator):
    """Concrete decorator - Chocolate Syrup topping."""

    def cost(self) -> float:
        return self._ice_cream.cost() + 10.0

    def description(self) -> str:
        return self._ice_cream.description() + ", Chocolate Syrup"


# Sprinkles topping
class Sprinkles(ToppingDecorator):
    """Concrete decorator - Sprinkles topping."""

    def cost(self) -> float:
        return self._ice_cream.cost() + 5.0

    def description(self) -> str:
        return self._ice_cream.description() + ", Sprinkles"


# Nuts topping
class Nuts(ToppingDecorator):
    """Concrete decorator - Nuts topping."""

    def cost(self) -> float:
        return self._ice_cream.cost() + 15.0

    def description(self) -> str:
        return self._ice_cream.description() + ", Nuts"
