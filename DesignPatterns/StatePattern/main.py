from VendingMachine import VendingMachine
from Product import Chocolate

if __name__ == "__main__":
    # Choose the product you want to use
    product = Chocolate()  # Change to IceCream() to dispense ice cream
    vending_machine = VendingMachine(product)

    # Testing the states
    vending_machine.insert_money()  # Insert money
    vending_machine.select_product()  # Select product
    vending_machine.insert_money()  # Attempt to insert money while dispensing