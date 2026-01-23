#!/usr/bin/python3
"""
This module provides a function to add two integers.
It performs type checking and casting for floats to integers.
The results are returned as the sum of the two numbers.
"""

def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98
    Returns:
        The addition of a and b as an integer.
    Raises:
        TypeError: If a or b are not integers, floats, or are Inf/NaN.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
