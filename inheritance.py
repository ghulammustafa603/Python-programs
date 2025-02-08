class Mammal:
    def walk(self):
        print("Can walk.")
class Dog(Mammal):
    def bark(self):
        print("woe woe!!")
class Cat(Mammal):
    def sound(self):
        print("miyanoow!!")
obj=Dog()
obj.walk()
obj.bark()
obj2=Cat()
obj2.sound()