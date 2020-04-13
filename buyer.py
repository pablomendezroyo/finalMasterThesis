from request import Request
from Interact_with_real_smart_contr import set_Money, get_balance

class Buyer:

    # batteryLevel
    def __init__(self, battery_Level):
        self.amount_kw =self.set_Amount()
        self.price_max_kwh = self.set_Price()
        self.balance = self._get_balance()

    def __str__(self):
        return "BUYER: amount_kw = {}, price_max_kwh = {}, balance = {}".format(self.amount_kw,  self.price_max_kwh, self.balance)

    def set_Price(self):
        request = Request()
        actual_price = request.price
        return actual_price + 2

    def set_Amount(self):
        amount = 2
        return amount

    def _get_balance(self):
        balance = get_balance()
        print("current balance: ", balance)
        balance = update_balance(balance)
        print("updated balance: ",update_balance)
        return balance

    def update_balance(self, balance):
        if(balance < self.amount_kw*self.price_max_kwh):
            set_Money(self.amount_kw*self.price_max_kwh - balance)
            updated_balance = get_balance()
            return updated_balance
        elif(balance >= self.amount_kw*self.price_max_kwh):
            return balance



def main():
    buyer = Buyer(1)
    print(buyer)

if __name__ == '__main__':
    main()

