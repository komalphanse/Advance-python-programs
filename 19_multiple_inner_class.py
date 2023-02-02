class doctors:
    def __init__(self):
        self.name='doctor'
        self.den=self.dentist()
        self.car=self.cardiologist()
    def show(self):
        print("in outre class")
        print("name:",self.name)
    class dentist:
        def __init__(self):
            self.name="dr. Savita"
            self.degree="BDS"
        def display(self):
            print("name:",self.name)
            print("degree:",self.degree)
    class cardiologist:
        def __init__(self):
            self.name="dr.amit"
            self.degree="dm"

        def display(self):
            print("name:",self.name)
            print("degree:",self.degree) 
outer=doctors()
outer.show()
d1=outer.den
d2=outer.car
print()
d1.display()
print()
d2.display()               


