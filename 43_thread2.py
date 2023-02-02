from threading import Thread
from time import sleep

def threaded_function(arg):
    for i in range(arg):
        print("running")
        sleep(1)
#if__name__="__main__"
t=threaded_function(10)
#thread=Thread(target=threaded_function,args=(10,))
#t.start()

#t.join()
print("thread finished...exiting")