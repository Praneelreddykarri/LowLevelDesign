# states/product_dispense_state.py
from State import State

class ProductDispenseState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_money(self):
        print("Product is being dispensed! Unable to insert money.")

    def select_product(self):
        print("Product is being dispensed! Unable to select a product.")

    def dispense(self):
        print("Dispensing the product...")
