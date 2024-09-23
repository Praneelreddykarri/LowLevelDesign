from Observer import Observer

class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self, stock, stock_price):
        for observer in self._observers:
            observer.update(stock, stock_price)
