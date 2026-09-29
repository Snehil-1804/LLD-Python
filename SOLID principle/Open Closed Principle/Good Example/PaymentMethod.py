from abc import ABC, abstractmethod

class PaymentMethod:
    @abstractmethod
    def pay(self,amount:int):
        pass

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying throug UPI of rs.{amount}")

class DebitCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying throug UPI of rs.{amount}")

class CreditcardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying throug UPI of rs.{amount}")

class PaymentProcess:
    def process_payment(self, paymentMethod:PaymentMethod,amount:int):
        paymentMethod.pay(amount)

debit= DebitCardPayment()
credit= CreditcardPayment()

paym_proc= PaymentProcess()
paym_proc.process_payment(debit,5000)
