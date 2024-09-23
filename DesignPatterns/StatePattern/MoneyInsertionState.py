from State import State

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
