from request import Request

class Buyer:
    def __init__(self):
        self.amount_kw =self.set_Amount()
        self.price_max_kwh = self.set_Price()
    def __str__(self):
        return "BUYER: amount_kw = {}, price_max_kwh = {}".format(self.amount_kw,  self.price_max_kwh)

    def set_Price(self):
        request = Request()
        actual_price = request.price
        return actual_price + 2

    def set_Amount(self):
        amount = 2
        return 5



def main():
    buyer = Buyer()
    print(buyer)

if __name__ == '__main__':
    main()

