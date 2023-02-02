class my_class:
    def instance_method(self):
        return "this is an instance"
obj=my_class()
print(obj.instance_method())


print("\n add other parameter with self")

class my_class1:
    def instance_method(self,a):
        return f"this is an instance method with a parameter a={a}."
obj1=my_class1()
print(obj1.instance_method(10))
print(my_class1.instance_method(10))   

print("\n")

