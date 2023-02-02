from threading import*
import time
import random
import queue
items=[]
def produce(c):
    while True:
        item=random.randint(1,10)
        print("producer producing Item:",item)
        q.put(item)
        print("producer giving Notification")
        time.sleep(5)
def consume(c):
    while True:
        print("consumer waiting for update")
        print("consumer consumed the item",q.get())
        time.sleep(5)
q=queue.Queue()
t1=Thread(target=consume,args=(q,))
t2=Thread(target=produce,args=(q,))
t1.start()
t2.start()                




