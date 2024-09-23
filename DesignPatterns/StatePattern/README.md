# State Design Pattern

## Overview

The State Design Pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class. This pattern is particularly useful when an object's behavior is influenced by its state, and the state can change at runtime.

## Use Case

The State Pattern is often used in scenarios where an object must change its behavior based on its current state. Common use cases include:

- Vending machines
- Game characters
- Traffic lights
- Workflow systems

## Vending Machine Example

### Context

Consider a vending machine that has three primary states:

1. **Money Insertion State**: The machine waits for the user to insert money.
2. **Product Selection State**: The user selects a product after inserting money.
3. **Product Dispense State**: The machine dispenses the selected product.

### Code Example

Here’s how the State Pattern can be implemented in a vending machine in Python, pls check the complete code in repository:

```python
# Abstract State Class
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_money(self):
        pass

    @abstractmethod
    def select_product(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


# Concrete State Classes
class MoneyInsertionState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Money inserted.")
        self.vending_machine.set_state(self.vending_machine.product_select_state)

    def select_product(self):
        print("Please insert money first!")

    def dispense(self):
        print("No product dispensed. Please insert money.")


class ProductSelectState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Money already inserted. Please select a product.")

    def select_product(self):
        print("Product selected.")
        self.vending_machine.set_state(self.vending_machine.product_dispense_state)

    def dispense(self):
        print("No product selected. Please select a product.")


class ProductDispenseState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Product is being dispensed! Unable to insert money.")

    def select_product(self):
        print("Product is being dispensed! Unable to select a product.")

    def dispense(self):
        product_name = self.vending_machine.product.get_name()
        print(f"Dispensing the {product_name}...")


# Vending Machine Class
class VendingMachine:
    def __init__(self, product):
        self.money_insertion_state = MoneyInsertionState(self)
        self.product_select_state = ProductSelectState(self)
        self.product_dispense_state = ProductDispenseState(self)
        self.current_state = self.money_insertion_state
        self.product = product  # Accept a product instance

    def set_state(self, state):
        self.current_state = state

    def insert_money(self):
        self.current_state.insert_money()

    def select_product(self):
        self.current_state.select_product()
        self.current_state.dispense()


# Running the vending machine
if __name__ == "__main__":
    product = Chocolate()  # Example product
    vending_machine = VendingMachine(product)
    
    # Testing the states
    vending_machine.insert_money()  # Insert money
    vending_machine.select_product()  # Select product
