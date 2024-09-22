from OrderState import CreatedState
from OrderNotifier import OrderNotifier


class Order:
    def __init__(self, user, orderID):
        """Initialize the Order object."""
        self.state = CreatedState()
        self.orderID = orderID
        self.user = user
        self.order_items = []
        self.total_amount = 0
        self.discounted_amount = 0
        self.notifier = OrderNotifier()  # Get the singleton instance

    def add_item(self, item, price):
        """Add an item to the order."""
        self.order_items.append({'item': item, 'price': price})
        self.total_amount += price

    def apply_coupon(self):
        """Apply a discount using the user's discount strategy."""
        discount_strategy = self.user.discount_strategy()
        self.discounted_amount = discount_strategy.apply_discount(self.total_amount)

    def next_state(self):
        """Proceed to the next state in the order lifecycle."""
        self.state.next_state(self)

    def notify(self, message):
        """Notify the user via the notifier."""
        self.notifier.notify(self.user.user_id, message)
