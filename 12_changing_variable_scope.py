x=20
def abc():
    x=40
    print(x)
abc()
print(x)    
print("\n modify value of list")
my_list=['hello','from','javapoint']
def func():
    my_list[1]='welcome to'

func()   
print(my_list)

print("\n modify the mylist in inner function")
my_list=['hello','from','javapoint']
def func():
    my_list=['a','b','c','d','f']
    return my_list
print(func())    

