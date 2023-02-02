import threading
import time
class myThread(threading.Thread):
    def __init__(self,id,name,counter):
        threading.Thread.__init__(self)
        self.id=id
        self.name=name
        self.counter=counter
    def run(self):
            print("starting",self.name)
            threadLock.aquire()
            print_time(self.name,self.counter,3)
            threadLock.release()
def print_time(threadname,delay,counter):
            while counter:
                time.sleep(delay)
                print("%s:%s"%(threadname,time.ctime(time.time())))
                counter -=1
threadLock=threading.Lock()
threads=[]
thread1=myThread(1,"Thread1",1)
thread2=myThread(2,"Thread2",2)
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)
for t in threads:
    t.join()
print("exiting main thread")    