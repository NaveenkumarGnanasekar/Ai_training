import math
class Shape:
    def area(self,lenght=None, width=0):
        pass
class circle(Shape):
    def area(self, lenght=None, width=0):
        super().area(lenght, width)
        if lenght == None:
            return math.pi * (width**2)
class rectangle(Shape):
    def area(self, lenght=None, width=0):
        super().area(lenght, width)
        if lenght :
            return lenght * width
shape= circle()
print(shape.area(None ,2))
shape1=rectangle()
print(shape1.area(2,4))