# products/product.py
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

class IceCream(Product):
    def __init__(self):
        self.name = "Ice Cream"
        self.price = 1.50

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class Chocolate(Product):
    def __init__(self):
        self.name = "Chocolate"
        self.price = 1.00

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price