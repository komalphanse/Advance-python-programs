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

def func(obj):
   obj.websites()
   obj.topic()
   obj.type()
obj1=xyz()
obj2=pqr()
func(obj1)
func(obj2)