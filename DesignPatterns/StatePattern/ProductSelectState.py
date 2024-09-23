from State import State

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
