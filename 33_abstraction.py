from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class toyota(car):
    def mileage(self):
        print("mileage of toyota is 25 kmph")
class suzuki(car):
      def mileage(self):
        print("mileage of suzuki is 30 kmph")   
class duster(car):
    def mileage(self):
        print("mileage of duster is 35 kmph")
class renault(car):
    def mileage(self):
        print("mileage of renault is 30 kmph")   
t=toyota()
t.mileage()
s=suzuki()
s.mileage()
d=duster()
d.mileage()
r=renault()
r.mileage()                       