# Observer Pattern

## Overview

The **Observer Pattern** is a behavioral design pattern where an object, called the **Subject**, maintains a list of dependents, called **Observers**, and automatically notifies them of any state changes. It defines a one-to-many relationship, ensuring that when the subject changes state, all its observers are notified and updated automatically.

This pattern is widely used in situations where an object needs to communicate with many other objects without needing to know their implementation details.

### Use Case Example:

Consider a stock market application. When the price of a stock changes, all investors who are interested in that stock (observers) should be notified of the price change. Here, the **Stock** is the **Subject**, and the **Investors** are the **Observers**.

## Key Components

- **Subject**: Maintains a list of observers and notifies them of state changes.
- **Observer**: Receives updates from the subject.
- **Concrete Observer**: A class that implements the observer and acts upon the received updates (e.g., `Investor`).

---

## Code Example: Stock Market System

### 1. Observer Interface

The `Observer` interface defines the `update` method, which will be called when the subject changes state.

```python
class Observer:
    # All observers must implement this method
    def update(self, stock, stock_price):
        pass
        
class Investor(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, stock, stock_price):
        print(f"{self.name} received update: {stock} stock price is now ${stock_price:.2f}")

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