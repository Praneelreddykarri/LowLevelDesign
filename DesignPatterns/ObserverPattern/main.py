from Stock import Stock
from Investor import Investor

if __name__ == "__main__":
    # Creating Stock instances
    apple_stock = Stock("Apple Inc.")
    google_stock = Stock("Google.")

    # Creating Investor instances
    investor1 = Investor("Alice")
    investor2 = Investor("Bob")
    investor3 = Investor("Praneel")

    # Registering investors to observe the stocks
    apple_stock.register_observer(investor1)
    apple_stock.register_observer(investor2)
    google_stock.register_observer(investor3)

    # Simulating stock price changes
    apple_stock.update_stock_price(150.00)
    apple_stock.update_stock_price(155.50)
    apple_stock.update_stock_price(149.75)

    google_stock.update_stock_price(200.00)