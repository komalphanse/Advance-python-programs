print("overriding __str__() method example")
class student:
    def __init__(self,name,rollno):
       self.name=name
       self.rollno=rollno
    def __str__(self):
        return "tis is student object name:{} and rollno:{}".format(self.name,self.rollno)   
s1=student("anushree",100)
s2=student('samarth',101)  
print(s1) #it will print the addresss of object
print(s2)     