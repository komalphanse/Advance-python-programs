print(len("komal"))
print(len([111,112,113,114,115,116]))

print("user define polymorphism")
def add(p,q,r=0):
    return p+q+r
print(add(6,23))
print(add(22,31,544))

print("\n polymorphism with class method")
class xyz():
    def websites(self):
        print("javapoint is a website out of many avaible on net.")
    def topic(self):
        print("python is out of many topics about technology on javapoint")
    def type(self):
        print("javapoint is an devoloped website.")
class pqr():                
    def websites(self):
        print("pinkvilla is a website out of many avaible on net.")
    def topic(self):
        print("celibrities is out of many topics")
    def type(self):
        print("pinkvilla is an devoloped website.")

obj_jtp=xyz()
obj_pvl=pqr()
for domain in (obj_jtp,obj_pvl):
    domain.websites()
    domain.topic()
    domain.type()

