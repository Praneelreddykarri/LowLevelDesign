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

Here's an Example of a vending machine using the State Pattern:

```plaintext

// Abstract State Class

class State {
    method insert_money()
    method select_product()
    method dispense()
}


// Concrete State Classes

class MoneyInsertionState extends State {
    method insert_money() {
        print("Money inserted.")
        set_state(ProductSelectState)
    }

    method select_product() {
        print("Please insert money first!")
    }

    method dispense() {
        print("No product dispensed. Please insert money.")
    }
}

class ProductSelectState extends State {
    method insert_money() {
        print("Money already inserted. Please select a product.")
    }

    method select_product() {
        print("Product selected.")
        set_state(ProductDispenseState)
    }

    method dispense() {
        print("No product selected. Please select a product.")
    }
}

class ProductDispenseState extends State {
    method insert_money() {
        print("Product is being dispensed! Unable to insert money.")
    }

    method select_product() {
        print("Product is being dispensed! Unable to select a product.")
    }

    method dispense() {
        print("Dispensing the product...")
    }
}


// Vending Machine Class

class VendingMachine {
    constructor(product) {
        this.state = MoneyInsertionState
    }

    method set_state(state) {
        this.state = state
    }

    method insert_money() {
        this.state.insert_money()
    }

    method select_product() {
        this.state.select_product()
        this.state.dispense()
    }
}


// Running the vending machine

vending_machine = new VendingMachine()
vending_machine.insert_money()  // User inserts money
vending_machine.select_product() // User selects a product
