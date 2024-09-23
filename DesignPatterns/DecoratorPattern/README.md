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

### Pseudo Code

```plaintext

// Component

interface IceCream {
    function cost(): Float
    function description(): String
}


// Concrete Component

class VanillaIceCream implements IceCream {
    function cost(): Float {
        return 50.0
    }
    function description(): String {
        return "Vanilla Ice Cream"
    }
}


// Decorator

abstract class ToppingDecorator implements IceCream {
    protected IceCream iceCream

    constructor(IceCream iceCream) {
        this.iceCream = iceCream
    }

    function cost(): Float {
        return this.iceCream.cost()
    }
    function description(): String {
        return this.iceCream.description()
    }
}


// Concrete Decorator

class ChocolateSyrup extends ToppingDecorator {
    function cost(): Float {
        return this.iceCream.cost() + 10.0
    }
    function description(): String {
        return this.iceCream.description() + ", Chocolate Syrup"
    }
}


// Client Code

function main() {
    IceCream iceCream = new VanillaIceCream()
    print(iceCream.description()) // "Vanilla Ice Cream"
    print(iceCream.cost())         // 50.0

    iceCream = new ChocolateSyrup(iceCream)
    print(iceCream.description()) // "Vanilla Ice Cream, Chocolate Syrup"
    print(iceCream.cost())         // 60.0
}
