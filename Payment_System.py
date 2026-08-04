from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card")


class UpiPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


print("Payment Methods")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

choice = int(input("Enter your choice: "))
amount = float(input("Enter amount: "))

if choice == 1:
    payment = CreditCardPayment()
elif choice == 2:
    payment = DebitCardPayment()
elif choice == 3:
    payment = UpiPayment()
else:
    print("Invalid Choice")
    exit()

processor = PaymentProcessor(payment)
processor.process_payment(amount)