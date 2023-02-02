from unicodedata import name


class Employee:
    count=0
    def __init__(self,name,id): #parameterized constructor
     self.id=id
     self.name=name
     Employee.count=Employee.count+1
    
    def display(self):
        print("ID:%d\nName:%s" %(self.id,self.name))
emp1=Employee("john",101)
emp2=Employee("David",102)
emp3=Employee("samu",103)
emp1.display()
emp2.display()
emp3.display()
print("the number of employee=",Employee.count)


class student:
    def __init__(self): #non parameterized constructor
        print("this is non parameterized constructor")
    def show(self,name):
        print("Hello",name)
st=student()
st.show("john")

#more than one constructor
class student1:
    def __init__(self):
        print("the 1st constructor")
    def __init__(self):
        print("the 2nd constructor")
    def __init__(sself):
        print("the 3rd constructor")
st1=student1()        
             

