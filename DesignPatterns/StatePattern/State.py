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
