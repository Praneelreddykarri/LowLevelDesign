from abc import ABC, abstractmethod
from DiscountStrategy import VIPDiscount, RegularDiscount, NoDiscount


class User(ABC):
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    @abstractmethod
    def discount_strategy(self):
        """Return the discount strategy associated with the user."""
        pass

class VipUser(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._user_type = "vip"

    def discount_strategy(self):
        """Return VIP discount strategy."""
        return VIPDiscount()  # Return VIP discount strategy


class RegularUser(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._user_type = "regular"

    def discount_strategy(self):
        """Return regular user discount strategy."""
        return RegularDiscount()  # Return Regular discount strategy