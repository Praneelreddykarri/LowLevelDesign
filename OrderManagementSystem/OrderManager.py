from OrderBuilder import OrderBuilder
from threading import Lock
from OrderState import DeliveredState


class OrderManager:
    """Manager for handling orders."""
    _order_counter = 0
    _lock = Lock()

    def __init__(self, notifier):
        self.notifier = notifier
        self.orders = []  # List to store active orders

    @classmethod
    def generate_order_id(cls):
        """Thread-safe order ID generation."""
        with cls._lock:
            cls._order_counter += 1
            return cls._order_counter

    def create_order(self, user, items):
        """Create and process an order for the given user."""
        order_id = self.generate_order_id()
        order_builder = OrderBuilder(user, order_id)

        for item, price in items:
            order_builder.add_item(item, price)

        order_builder.apply_coupon()
        order = order_builder.build()
        self.orders.append(order)  # Store the order

        self.print_orders(order)
        order.next_state()  # Move to the next state

        # This is optional, if you don't want to store the order history then we can use below code
        # if isinstance(order.state, DeliveredState):
        #     self.remove_order(order)

        return order

    def remove_order(self, order):
        """Remove the order from the active orders list once processed."""
        if order in self.orders:
            self.orders.remove(order)
            print(f"Order for user {order.user.user_id} has been removed after processing.")

    def print_orders(self, order):
        """Print details of the order."""
        print("New Order Placed")
        print(f"Order ID: {order.orderID}", end="\n\n")
        print(f"Items: {order.order_items}", end="\n\n")
