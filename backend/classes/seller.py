from request.request import Request
from config import address_account_1, private_key_1

class Seller:
    # batteryLevel
    def __init__(self):
        self.amount_min_kw, self.amount_max_kw = self.set_amounts() 
        self.price_min_kwh = self.set_Price()

    def __str__(self):
        return "SELLER: amount_min_kw = {}, amount_max_kw = {}, price_min_kwh = {}".format(self.amount_min_kw, self.amount_max_kw, self.price_min_kwh)

    def set_amounts(self):
        print("Please, set the minimum amount of Kw you would like to sell: ")
        _amount_min_kw = int(input())
        print("Please, set the maximum amount of Kw you would like to sell")
        _amount_max_kw = int(input())
        return _amount_min_kw, _amount_max_kw
    
    def set_Price(self):
        request = Request()
        actual_price = request.price
        print("The actual price in the market is: {}, at what price would you want to sell?".format(actual_price))
        price_to_buy = int(input())
        return price_to_buy

def main():
    seller = Seller(98)
    print(seller)

if __name__ == '__main__':
    main()

    