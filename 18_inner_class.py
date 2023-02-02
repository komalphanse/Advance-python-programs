
class colour:
    def __init__(self):
        self.name= "green"
        self.lg=self.lightgreen()
    def show(self):
          print("colour name:",self.name)

    class lightgreen:
        def __init__(self):
            self.name="lightgreen"
            self.code="c12ad"
        def display(self):
            print("colour name:",self.name)
            print("colour code:",self.code)
outer=colour()
outer.show()           
g=outer.lg
g.display()    