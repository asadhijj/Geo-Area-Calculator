import pytest
from geo_calc import geo

# testing the main shape
def test_shape_area():
    shape = geo.Shape(3, 4)
    assert shape.get_area() == 12

# testing the str output
def test_shape_str():
    shape = geo.Shape(3, 4)
    assert shape.__str__() == 'The area of Shape is 12.00'

# testing the rectangle area
def test_rectangle_area():
    shape = geo.Rectangle(4, 4)
    assert shape.get_area() == 16

# testing the triangle area
def test_triangle_area():
    shape = geo.Triangle(3, 4)
    assert shape.get_area() == 6

# testing the square area
def test_square_area():
    shape = geo.Square(3,3)
    assert shape.get_area() == 9

# testing the circle area
def test_Circle_area():
    shape = geo.Circle(3)
    assert shape.get_area() == 28.274333882308138

# testing the hexagon area
def test_Hexagon_area():
    shape = geo.Hexagon(3)
    assert shape.get_area() == 23.382685902179844
