import pytest
from geo_calc import geo


def test_shape_area():
    shape = geo.Shape(3, 4)
    assert shape.get_area() == 12


def test_shape_str():
    shape = geo.Shape(3, 4)
    assert shape.__str__() == 'The area of Shape is 12.00'


def test_rectangle_area():
    shape = geo.Rectangle(4, 4)
    assert shape.get_area() == 16


def test_triangle_area():
    shape = geo.Triangle(3, 4)
    assert shape.get_area() == 6


def test_square_area():
    shape = geo.Square(3)
    assert shape.get_area() == 9


def test_Circle_area():
    shape = geo.Circle(3)
    assert shape.get_area() == 28.274333882308138


def test_Hexagon_area():
    shape = geo.Hexagon(3)
    assert shape.get_area() == 23.382685902179844
