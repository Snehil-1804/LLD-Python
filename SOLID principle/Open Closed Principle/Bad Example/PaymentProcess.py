class PaymentProcess:
    def pay(self, payment_method: str, amount: int):
        if payment_method=="UPI":
            print(f"Stating the payment of Rs.{amount}")
            print(f"UPI Transcation fininshed")
        if payment_method=="credit":
            print(f"Stating the payment of Rs.{amount}")
            print(f"UPI Transcation fininshed")
        if payment_method=="net":
            print(f"Stating the payment of Rs.{amount}")
            print(f"UPI Transcation fininshed")

pay_u=PaymentProcess()
pay_u.pay("UPI",5000)