print("polymorphism with inheritance")
class Birds:
     def intro1(self):
        print("there are multiple types of birds in the  world")
     def flight1(self):
         print("many of these birds can fly but some cannot")
class sparrow1(Birds):
    def flight1(self):
        print("sparow are birds which can fly")
class ostrich1(Birds):
    def flight1(self):
        print("ostriches are the birds which cannot fly")
obj1=Birds()
obj2=sparrow1()
obj3=ostrich1()

obj1.intro1()
obj1.flight1()

obj2.intro1()
obj2.flight1()

obj3.intro1()
obj3.flight1()