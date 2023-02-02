class calculation1:
    def sum(self,a,b):
        return a+b
class calculation2:
    def multi(self,a,b):
        return a*b 
class derived(calculation1,calculation2):
    def divide(self,a,b):
      return a/b 
d=derived() 
print(d.sum(10,20))
print(d.multi(10,20))
print(d.divide(10,20))
print(issubclass(derived,calculation2))
print(issubclass(calculation1,calculation2))                 
print(isinstance(d,derived))