import time
import queue

from backend.classes.seller import Seller
from backend.classes.buyer import Buyer
from backend.smartContract_Interaction.Interact_with_real_smart_contr import set_Buyer, set_Seller
from backend.threads.thread_event import myThread
from backend.config import topic_account_1, topic_account_2, address_account_1, private_key_1

STATUS = ""

while(1):

    print("Insert battery Level: ")
    battery_level = int(input())
    battery_level_min = 20
    battery_level_max = 80

    print("Battery level: {}, battery max level: {}, battery min level: {}".format(battery_level, battery_level_max, battery_level_min))

    if(battery_level < battery_level_min):
        buyer = Buyer(battery_level)
        print(buyer)
        set_Buyer(address_account_1, private_key_1, buyer.amount_kw, buyer.price_max_kwh)

        STATUS = 'BUYER'

        #Qeue
        my_queue = queue.Queue()
        # Create new threads
        thread1 = myThread(topic_account_1, None, my_queue)
        # Start new Threads
        thread1.start()
        thread1.join()
        # Data from threads in qeue
        my_amount_kw = my_queue.get_nowait()
        my_total_money = my_queue.get_nowait()
        print("TRANSACTION DONE: Amount_kw = {} , Money interchange = {}".format(my_amount_kw, my_total_money))
        battery_level += my_amount_kw

    elif(battery_level > battery_level_max):
        seller = Seller(battery_level)
        print(seller)
        set_Seller(address_account_1, private_key_1, seller.amount_min_kw, seller.amount_max_kw, seller.price_min_kwh)

        STATUS = 'SELLER'
        
        #Qeue
        my_queue = queue.Queue()
        # Create new threads
        thread1 = myThread(None, topic_account_1, my_queue)
        # Start new Threads
        thread1.start()
        thread1.join()
        # Data from threads in qeue
        my_amount_kw = my_queue.get_nowait()
        my_total_money = my_queue.get_nowait()
        print("TRANSACTION DONE: Amount_kw = {} , Money interchange = {}".format(my_amount_kw, my_total_money))
        battery_level -= my_amount_kw

    else:
        print("Battery Level: ", battery_level)
        STATUS = ""
    
    time.sleep(60)