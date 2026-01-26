#!/usr/bin/python3
"""
This module provides a Square class for geometric calculations.
It serves as a foundation for representing square shapes in a 2D plane.
"""


class Square:
    """
    Defines a square shape and manages its attributes and behavior.
    This class is currently a placeholder for future square-related logic.
    """
    def __init__(self, size=0, position = (0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Getter: Retrieves the private __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter: Sets the private __size with validation logic.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter: Retrieves the private __position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter: Sets the private __position with validation logic.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        return the current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        print in stdout the square with the character '#'
        """
        if self.size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
