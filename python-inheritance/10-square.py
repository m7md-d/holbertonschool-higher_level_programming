#!/usr/bin/python3
"""
Module that defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that defines a square, inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        super().__init__(size, size)

        self.__size = size

    def area(self):
        """
        Return the area of the Square.
        """
        return self.__size ** 2
