from Subject import Subject


class Stock:
    def __init__(self, name):
        self.name = name
        self.price_subject = Subject()
        self._stock_price = 0.0

    def register_observer(self, observer):
        self.price_subject.register_observer(observer)

    def remove_observer(self, observer):
        self.price_subject.remove_observer(observer)

    def update_stock_price(self, price):
        self._stock_price = price
        self.price_subject.notify_observers(self.name,self._stock_price)