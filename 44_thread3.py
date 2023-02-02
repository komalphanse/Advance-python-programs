import threading 
import time 
class myThread(threading.Thread):
    def __init__(self,threadid,name,counter):
        threading.Thread.__init__(self)
        self.threadid=threadid
        self.name=name
        self.counter=counter
    def run(self):
        print("staring",self.name)
        lock.acquire()
        print(self.name,self.counter,3)
        lock.release() 
    def display(threadName,delay,counter):
        while counter:
            time.sleep(delay)
            print("%s:%s"%(threadName,time.ctime(time.time())))
            counter-=1
            
lock=threading.Lock()

#creat new thread
t1=myThread(1,"Thread1",1)
t2=myThread(2,"Thread2",2)
#start new threads
t1.start()
t2.start()

t1.display(1,3)
t2.display(2,3)

t1.join()
t2.join()
print("EXIT")