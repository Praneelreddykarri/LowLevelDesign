from Observer import Observer

class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, stock, stock_price):
        print(f"{self.name} received update: {stock} stock price is now ${stock_price:.2f}")
