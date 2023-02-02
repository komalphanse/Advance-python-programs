from abc import ABC,abstractmethod
class polygoan(ABC):
    @abstractmethod
    def sides(self):
        pass
class triangle(polygoan):
    def sides(self):
        print("triangle has 3 sides")
class pentagoan(polygoan):
      def sides(self):
        print("triangle has 5 sides")   
class hexagoan(polygoan):
    def sides(self):
        print("triangle has 6 sides")
class square(polygoan):
    def sides(self):
        print("triangle has 4 sides")   
t=triangle()
t.sides()
p=pentagoan()
p.sides()
h=hexagoan()
h.sides()
s=square()
s.sides()                       
