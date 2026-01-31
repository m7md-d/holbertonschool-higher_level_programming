#!/usr/bin/python3
"""
Module to demonstrate Abstract Base Classes and Duck Typing in Python.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all geometric shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete implementation of a Circle.
    """

    def __init__(self, radius):
        """
        Initialize a new Circle.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the Circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Return the perimeter (circumference) of the Circle.
        """
        return abs(2 * math.pi * self.radius)


class Rectangle(Shape):
    """
    Concrete implementation of a Rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Return the area of the Rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the Rectangle.
        """
        return abs(2 * (self.width + self.height))


def shape_info(shape):
    """
    Prints area and perimeter of a shape using duck typing.
    Expects 'shape' to have area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
