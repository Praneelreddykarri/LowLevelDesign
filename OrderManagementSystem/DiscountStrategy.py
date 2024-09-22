from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total_amount):
        pass

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, total_amount):
        return total_amount * 0.9  # 10% discount for VIPs


class RegularDiscount(DiscountStrategy):
    def apply_discount(self, total_amount):
        return total_amount * 0.95  # 5% discount for Regular customers


class NoDiscount(DiscountStrategy):
    def apply_discount(self, total_amount):
        return total_amount  # No discount applied

