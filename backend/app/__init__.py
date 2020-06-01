import time
import queue
import RPi.GPIO as GPIO

from classes.seller import Seller
from classes.buyer import Buyer
from smartContract_Interaction.Interact_with_real_smart_contr import set_Buyer, set_Seller
from threads.thread_event import myThread
from config import topic_account_1, topic_account_2, address_account_1, private_key_1, address_account_2, private_key_2

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode (starts in low)

while(1):

    print("Select an option: option 1 - SELL kw, option 2 - BUY kw, option 3 - nothing")
    option = int(input())

    print("Option selected: ", option)

    if(option == 2):
        buyer = Buyer()
        print(buyer)
        set_Buyer(address_account_1, private_key_1, buyer.amount_kw, buyer.price_max_kwh)

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
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
        time.sleep(4)
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
        print("Going to sleep...")

    elif(option == 1):
        seller = Seller()
        print(seller)
        set_Seller(address_account_1, private_key_1, seller.amount_min_kw, seller.amount_max_kw, seller.price_min_kwh)
        
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
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
        time.sleep(4)
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
        print("Going to sleep...")

    elif(option == 3):
        pass

    
    else:
        print("Please, select a correct option")
    
    time.sleep(30)