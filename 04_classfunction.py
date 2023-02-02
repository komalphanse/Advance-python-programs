class student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
    def display (self):
        print("Name:%s,ID:%d,age:%d"%(self.name,self.id,self.age))
s=student("john",101,25)
print(s.__doc__)
print(s.__dict__)
print(s.__module__)

print("Built in class functions")
print(getattr(s,'name')) 
print(getattr(s,'age'))
setattr(s,"age",22)
print(getattr(s,'age'))  
print(hasattr(s,'id')) 
delattr(s,'age')   
print("age attribute will be deleted by delattr function") 
      