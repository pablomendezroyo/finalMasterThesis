import threading
import time
from Interact_with_real_smart_contr import listen_to_events

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, counter):
      threading.Thread.__init__(self)
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      listen_to_events()
      print("Exiting " + self.name)



def main():
    # Create new threads
    thread1 = myThread(1)

    # Start new Threads
    thread1.start()



if __name__ == '__main__':
    main()
