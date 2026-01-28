#!/usr/bin/python3
"""
Simple rectangle!
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width set
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height set
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        return the rectangle perimeter
        """
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        return string of the rectangle with the character #
        """
        if (self.__height == 0 or self.__width == 0):
            return ""
        moraba3 = ""
        c = ""
        for i in range(self.__height):
            moraba3 + c
            moraba3 + ("#" * self.__width)
            c = "\n"
        return moraba3

    def __repr__(self):
        """
        return a string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"
