from threading import*
def fun():
    print("geeks for geeks")
T=Thread(target=fun)
print("GFG")
print(T.isDaemon())
T.setDaemon(True)
print(T.isDaemon())
T.start()    