class Animal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def cat(self):
        print("Four legs.")

    def hen(self):
        print("two legs.")


obj1=Animal(3,4)
obj1.cat()
obj1.x=34
obj1.y=3434

print(obj1.x)
print(obj1.y)
print(obj1.a)