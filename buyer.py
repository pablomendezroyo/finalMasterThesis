from request import Request
from Interact_with_real_smart_contr import set_Money, get_balance_received
from config import address_account_1, private_key_1

class Buyer:

    # batteryLevel
    def __init__(self, battery_Level):
        self.battery_level = battery_Level
        self.amount_kw =self.set_amount_kw()
        self.price_max_kwh = self.set_Price()
        self.balance = self._get_balance()

    def __str__(self):
        return "BUYER: amount_kw = {}, price_max_kwh = {}, balance = {}".format(self.amount_kw,  self.price_max_kwh, self.balance)

    def set_Price(self):
        request = Request()
        actual_price = request.price
        return actual_price + 2

    def set_amount_kw(self):
        amount = 50 - self.battery_level
        return amount

    def _get_balance(self):
        balance = get_balance_received(address_account_1)
        print("current balance: ", balance)
        print(address_account_1, private_key_1, self.amount_kw*self.price_max_kwh)
        if(balance < self.amount_kw*self.price_max_kwh):
            set_Money(address_account_1, private_key_1, self.amount_kw*self.price_max_kwh - float(balance))
            updated_balance = get_balance_received(address_account_1)
            print("updated balance: ", updated_balance)
            return updated_balance
        elif(balance >= self.amount_kw*self.price_max_kwh):
            print("current balance: ", balance)
            return balance

def main():
    buyer = Buyer(11)
    print(buyer)

if __name__ == '__main__':
    main()

