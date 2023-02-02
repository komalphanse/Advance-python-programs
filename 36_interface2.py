print("1 interface and 2 sub classes to that interface")
from abc import*
class dbinterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
class oracle(dbinterface):
    def connect(self):
      print("oracle detabace is connected")
    def disconnect(self):
        print("oracle database disconnected")
class sybase(dbinterface):
    def connect(self):
      print("mysql detabace is connected")
    def disconnect(self):
        print("mysql database disconnected")  
dbname=input("enter databace name either oracle or sybase:")  
classname=globals()[dbname] 
x=classname()
x.connect() 
x.disconnect()      

        