from MoneyInsertionState import MoneyInsertionState
from ProductSelectState import ProductSelectState
from ProductDispenseState import ProductDispenseState

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