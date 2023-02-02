class abc:
    def __init__(self):
        self.inner=self.Inner()
    def show(self):
        print("this is an outer class")
    class Inner:
        def __init__(self):
            self.innerclassofinner=self.Innerclassofinner()
        def show(self):
            print("this is the inner class")
        class Innerclassofinner:
            def show(self):
                print("tis is an inner class of inner class")
outer=abc()
outer.show()
print()
gfg1=outer.inner
gfg1.show()
print()
gfg2=outer.inner.innerclassofinner
gfg2.show()                             