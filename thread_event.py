import threading
import time
from Interact_with_real_smart_contr import listen_to_events
from config import topic_account_1, topic_account_2


class myThread (threading.Thread):
   def __init__(self, _topic_buyer, _topic_seller):
      threading.Thread.__init__(self)
      self._topic_buyer = _topic_buyer
      self._topic_seller = _topic_seller

   def run(self):
      print("Starting ")
      listen_to_events(self._topic_buyer, self._topic_seller)
      print("Exiting ")



def main():
    # Create new threads
    thread1 = myThread(topic_account_1, None)

    # Start new Threads
    thread1.start()



if __name__ == '__main__':
    main()
