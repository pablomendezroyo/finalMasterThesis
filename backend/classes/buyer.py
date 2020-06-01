from request.request import Request
from smartContract_Interaction.Interact_with_real_smart_contr import set_Money, get_balance_received
from config import address_account_1, private_key_1

class Buyer:

    # batteryLevel
    def __init__(self):
        self.amount_kw =self.set_amount_kw()
        self.price_max_kwh = self.set_Price()
        self.balance = self._get_balance()

    def __str__(self):
        return "BUYER: amount_kw = {}, price_max_kwh = {}, balance = {}".format(self.amount_kw,  self.price_max_kwh, self.balance)

    def set_Price(self):
        request = Request()
        actual_price = request.price
        print("The actual price in the market is: {}, at what price would you want to buy?".format(actual_price))
        price_to_sell = int(input())
        return price_to_sell

    def set_amount_kw(self):
        print("Please, set an amount of kw to buy: ")
        amount = int(input())
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

