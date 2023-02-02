class employee:
    id=10
    name="devansh"
    def display(self):
        print("emp_id=",self.id ,"emp_name=",self.name)
a1=employee()
a1.display()
#deleting the property of object

del a1.id
#deleting the object itself
del a1