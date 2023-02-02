class abc:
    def __init__(self):
        self.course="campus preparation"
        self.duration="2 months"
    def show(self):
        print("course:",self.course)
        print("duration:",self.duration)

outer=abc()
outer.show()            