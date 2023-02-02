print(" interface having 2 abstract method or 1base class ")
from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def balance_check(self):
      pass
    @abstractmethod  
    def intrest(self):
      pass
class SBI(bank):
    def balance_check(self):
     print("balance is 100 rs.")
    
    def intrest(self):
      print("sbi bank intrest is 5 rs.")

b=SBI()
b.balance_check()
b.intrest()      