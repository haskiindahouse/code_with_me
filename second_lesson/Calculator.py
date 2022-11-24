"""
+ - / * = . +/- ac
"""


class Shape:
    def hello(self):
        print("im shape")


class Triangle(Shape):
    def __init__(self, a, b, c):
        print("i was born")
        self._a = a
        self.b = b
        self.c = c

    def hello(self):
        print(self._a, self.b, self.c)

class Rectangle(Shape):
    pass

myTriangle = Triangle(4, 3, 5)
myTriangle.hello()
rect = Rectangle()
rect.hello()