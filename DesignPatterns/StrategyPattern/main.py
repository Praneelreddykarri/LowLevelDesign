from PaymentProcessor import PaymentProcessor
from CreditCardPayment import CreditCardPayment
from PayPalPayment import PayPalPayment
from BitcoinPayment import BitcoinPayment

if __name__ == "__main__":
    # Example payment amounts
    amount = 100.50

    # Credit Card Payment
    credit_card_payment = CreditCardPayment("1234-5678-9876-5432")
    payment_processor = PaymentProcessor(credit_card_payment)
    payment_processor.process_payment(amount)

    # Change strategy to PayPal
    paypal_payment = PayPalPayment("user@example.com")
    payment_processor.set_strategy(paypal_payment)
    payment_processor.process_payment(amount)

    # Change strategy to Bitcoin
    bitcoin_payment = BitcoinPayment("1BitcoinAddress123")
    payment_processor.set_strategy(bitcoin_payment)
    payment_processor.process_payment(amount)
