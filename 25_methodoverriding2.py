class bank:
    def getroi(self):
     return 10
class SBI(bank): 
    def getroi(self):
     return 7

class ICICI(bank):
    def getroi(self):
     return 8 
b1=bank()
b2=SBI()
b3=ICICI()
print("bank rate of intrest=",b1.getroi()) 
print("SBI rate of intrest=",b2.getroi())
print("ICICI rate of intrest=",b3.getroi())                       
