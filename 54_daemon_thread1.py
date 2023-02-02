from threading import*
import time
def thread_1():
    for i in range(5):
        print("this is thread T")
        time.sleep(3)
T=Thread(target=thread_1)
T.setDaemon(True)
T.start()
time.sleep(5)
print("this is main Thread")