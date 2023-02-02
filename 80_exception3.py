#python code to catch an exception and handle it using try and except code blocks
a=["python","exceptions","try and except"]
try:
    #looping through the elements of the array a,choosing a range that goes beyond thelength of the array
    for i in range(4):
        print("the index and element from the array is",i,a[i])
        # if an error occure in the try block,then except block will be executed by the python interpreter
except:
       print("index out of range")
