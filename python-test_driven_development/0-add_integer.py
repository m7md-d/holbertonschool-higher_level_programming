#!/usr/bin/python3

"""
This module provides a function to add two integers.
It performs type checking and casting for floats to integers.
The results are returned as the sum of the two numbers.
"""
def add_integer(a, b=98):
    """
    Adds two integers. Floats are casted to integers.
    Raises TypeError if a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
