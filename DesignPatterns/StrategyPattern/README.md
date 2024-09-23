# Strategy Pattern Explained

## Overview
The **Strategy Pattern** is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one as a separate class, and make them interchangeable. This pattern lets the algorithm vary independently from the clients that use it.

In simpler terms, it enables selecting different algorithms (or behaviors) at runtime without altering the client code. It helps in making your code flexible and open to future changes without requiring modifications to existing code.

### Key Benefits of the Strategy Pattern:
- **Separation of Concerns**: Each strategy is encapsulated in its own class, making the code easier to understand and maintain.
- **Interchangeability**: Strategies can be swapped easily at runtime.
- **Extensibility**: New strategies can be added without modifying existing code, adhering to the Open/Closed Principle of SOLID.

## How It Works
In the Strategy Pattern, there are three main components:
1. **Context**: The class that uses a strategy to perform its function. In your code, this is the `PaymentProcessor` class.
2. **Strategy**: The interface or abstract class that declares the method(s) to be implemented by all concrete strategies. In your code, this is the `PaymentStrategy` abstract class.
3. **Concrete Strategies**: These are the specific implementations of the `Strategy`. In your code, examples are `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment`.

## Example from the Code

Here’s a small example that shows how the Strategy Pattern is applied (check full code in the repository):

```python
# Changing payment strategy at runtime
credit_card_payment = CreditCardPayment("1234-5678-9876-5432")
payment_processor = PaymentProcessor(credit_card_payment)
payment_processor.process_payment(100.50)

# Changing the strategy to PayPal
paypal_payment = PayPalPayment("user@example.com")
payment_processor.set_strategy(paypal_payment)
payment_processor.process_payment(100.50)
