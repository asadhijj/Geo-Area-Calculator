from math import pi, sqrt


class Shape:
    def __init__(self, side1, side2=None):
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        # This function returns the area of the shape
        return self.side1 * self.side2

    def __str__(self):
        # It allows you to modify the way an instance will print.
        return (f'The area of {self.__class__.__name__} is {self.get_area():,.2f}')
        # The self.__class__.__name__ hidden attribute refers to the name of the class.
        # If you were working with a Triangle class, that attribute would be “Triangle.”


class Rectangle(Shape):
    '''a class that takes the values for the recatngle'''
    def __init__(self, side1, side2):
        super().__init__(side1, side2)


class Square(Shape):
    '''a class that takes the values for the Square'''
    def __init__(self, side1, side2):
        super().__init__(side1, side2)


class Triangle(Shape):
    '''a class that takes the values for the Triangle'''
    def __init__(self, base, height):
        super().__init__(side1=base, side2=height)

    def get_area(self):
        # A method defined in the superclass is called and the result is stored as a variable
        area = super().get_area()
        return area / 2


class Circle(Shape):
    '''a class that takes the values for the circle'''
    def __init__(self, radius):
        super().__init__(side1=radius)

    def get_area(self):
        return pi * pow(self.side1, 2)


class Hexagon(Shape):
    '''a class that takes the values for the regular hexagon'''
    def __init__(self, side):
        super().__init__(side)

    def get_area(self):
        return (3 * sqrt(3) * self.side1 ** 2) / 2