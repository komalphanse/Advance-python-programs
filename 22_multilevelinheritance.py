class animal:
    def speak(self):
        print("animal speaking")
class dog(animal):
    def bark(self):
        print("dog barking")
class puppy(dog):
    def eat(self):
        print("eating bread")
            
d=puppy()
d.speak()
d.bark() 
d.eat()       
