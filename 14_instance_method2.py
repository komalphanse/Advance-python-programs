print("\n instance method using constructor")
class my_class:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def instance_method(self):
        return f"this is the instance method and it can access the variables a={self.a} and b={self.b}with the help of self."
obj=my_class(2,4)
print(obj.instance_method())
