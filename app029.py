# comments in python and classes in python
# numbers. strings, booleans, list and dictionaries
# pascal naming convention, upper letter leads , if mutiple words, 'EmailClien'
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

# create another oject
point2 = Point()
point2.x = 40
