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
