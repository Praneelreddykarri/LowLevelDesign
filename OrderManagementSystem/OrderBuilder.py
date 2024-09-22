from Order import Order

class OrderBuilder:
    def __init__(self, user,orderID):
        self.order = Order(user,orderID)

    def add_item(self, item, price):
        self.order.add_item(item, price)
        return self

    def apply_coupon(self):
        self.order.apply_coupon()
        return self

    def build(self):
        return self.order
