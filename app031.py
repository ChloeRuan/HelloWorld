# inheritance in python
"""
class Dog:
    def walk(self):
        print("walk")


class Cat:
    def walk(self):
        print("walk")
"""


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


#  pass    # mean nothing, just pass this line


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.be_annoying()
