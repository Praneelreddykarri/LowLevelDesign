# Decorator Design Pattern

## Overview

The Decorator Pattern is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class. This pattern is typically used to adhere to the Single Responsibility Principle by allowing functionality to be divided among classes with unique areas of concern.

## Key Components

1. **Component**: An interface or abstract class defining the methods that can be implemented.
2. **Concrete Component**: A class that implements the component interface. This class is the object that will be decorated.
3. **Decorator**: An abstract class that implements the component interface and contains a reference to a component object. This class adds functionality to the component.
4. **Concrete Decorators**: Classes that extend the decorator class to add additional functionality or behavior.

## Benefits

- **Flexibility**: You can add or remove functionalities at runtime.
- **Reusability**: Each decorator can be reused across different components.
- **Adheres to Open/Closed Principle**: Classes are open for extension but closed for modification.

## Example

### Scenario: Ice Cream Shop

Consider a scenario where we have different types of ice creams and we want to add toppings (like chocolate syrup, sprinkles, and nuts) dynamically.

### Example Code

```plaintext
# Component

class IceCream:
    def cost(self) -> float:
        pass

    def description(self) -> str:
        pass


# Concrete Component

class VanillaIceCream(IceCream):
    def cost(self) -> float:
        return 50.0

    def description(self) -> str:
        return "Vanilla Ice Cream"


# Decorator

class ToppingDecorator(IceCream):
    def __init__(self, ice_cream: IceCream):
        self._ice_cream = ice_cream

    def cost(self) -> float:
        return self._ice_cream.cost()

    def description(self) -> str:
        return self._ice_cream.description()


# Concrete Decorator

class ChocolateSyrup(ToppingDecorator):
    def cost(self) -> float:
        return self._ice_cream.cost() + 10.0

    def description(self) -> str:
        return self._ice_cream.description() + ", Chocolate Syrup"


# Client Code

def main():
    ice_cream = VanillaIceCream()
    print(ice_cream.description())  # "Vanilla Ice Cream"
    print(ice_cream.cost())          # 50.0

    ice_cream = ChocolateSyrup(ice_cream)
    print(ice_cream.description())  # "Vanilla Ice Cream, Chocolate Syrup"
    print(ice_cream.cost())          # 60.0