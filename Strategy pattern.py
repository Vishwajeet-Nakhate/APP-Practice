# Strategy Pattern Example

# Strategy 1
class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# Strategy 2
class UpiPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Strategy 3
class CashPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")


# Context
class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# Using Credit Card
payment = Payment(CreditCardPayment())
payment.make_payment(500)

# Using UPI
payment = Payment(UpiPayment())
payment.make_payment(1000)

# Using Cash
payment = Payment(CashPayment())
payment.make_payment(300)
