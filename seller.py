from request import Request

class Seller:
    
    # batteryLevel
    def __init__(self):
        self.amount_min_kw, self.amount_max_kw = self.set_amounts() 
        self.price_min_kwh = self.set_Price()

    def __str__(self):
        return "SELLER: amount_min_kw = {}, amount_max_kw = {}, price_min_kwh = {}".format(self.amount_min_kw, self.amount_max_kw, self.price_min_kwh)

    def set_amounts(self):
        _amount_min_kw = 1
        _amount_max_kw = 3
        return _amount_min_kw, _amount_max_kw
    
    def set_Price(self):
        request = Request()
        actual_price = request.price
        return actual_price - 2

def main():
    seller = Seller()
    print(seller)

if __name__ == '__main__':
    main()

    