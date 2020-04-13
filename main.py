import time

from seller import Seller
from buyer import Buyer
from Interact_with_real_smart_contr import set_Buyer, set_Seller

while(1):
    battery_level = 35
    battery_level_min = 20
    battery_level_max = 80

    if(battery_level < battery_level_min):
        buyer = Buyer(battery_level)
        set_Buyer(buyer.amount_kw, buyer.price_max_kwh)

    elif(battery_level > battery_level_max):
        seller = Seller(battery_level)
        set_Seller(seller.amount_min_kw, seller.amount_mak_kw, seller.price_min_kwh)

    else:
        pass
    
    time.sleep(30)