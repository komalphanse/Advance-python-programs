print("inter thread communication by using event object")

from threading import *
import time
def traffic_police():
    while True:
        time.sleep(5)
        print("trafic police giving green signal")
        event.set() 
        time.sleep(10)
        print("trafic police giving red signal")
        event.clear()
def driver():
    num=0
    while True:
        print("driving waiting for green signal")
        event.wait()
        print("traffic signal is green...vehicles can move")
        while event.isSet():
            num=num+1
            print("vehicle no:",num,"crossing the signal")   
event=Event()
t1=Thread(target=traffic_police) 
t2=Thread(target=driver)
t1.start()
t2.start()                
t2.start()                