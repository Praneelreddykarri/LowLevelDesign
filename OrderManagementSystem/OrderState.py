from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def next_state(self, order):
        pass

class CreatedState(OrderState):
    def next_state(self, order):
        order.notify("Order has been confirmed!")
        order.state = ProcessState()
        order.next_state()

class ProcessState(OrderState):
    def next_state(self, order):
        order.notify("Your Order is being processed!")
        order.state = ConfirmedState()
        order.next_state()

class ConfirmedState(OrderState):
    def next_state(self, order):
        order.notify("Order has been dispatched!")
        order.state = DispatchedState()
        order.next_state()

class DispatchedState(OrderState):
    def next_state(self, order):
        order.notify("Order is Out for delivery!")
        order.state = DeliveredState()
        order.next_state()

class DeliveredState(OrderState):
    def next_state(self, order):
        order.notify("Order delivered!")
