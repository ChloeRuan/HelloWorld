# built in modules in python so you can import directly
import random

# it generates random values between 0 and 1
for i in range(3):
    print(random.random())

# for dozens
for i in range(3):
    print(random.randint(10, 20))

# another method to randomly pick up an item from a list
members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


# exercise
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return (first, second)


# for return, you dont have to include (), as python will aotumatically interprete it as tuples
dice = Dice()
print(dice.roll())
