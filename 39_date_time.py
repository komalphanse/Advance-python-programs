import time 
#prints the no.of ticks spent 12am in 1jan 1970
print(time.time())
#returns a time in tuple
print(time.localtime(time.time()))
#returns the formated time
print(time.asctime(time.localtime(time.time())))
for i in range(0,5):
    print(i)
    time.sleep(1)#each element will be printed after 1 second