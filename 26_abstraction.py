class Employee:
    _count=0
    def __init__(self):
        Employee._count=Employee._count+1
    def display(self):
        print("enter no. of employee=",Employee._count)
emp=Employee()
emp2=Employee()
try:
    print(emp._count)
finally:
    emp.display()            