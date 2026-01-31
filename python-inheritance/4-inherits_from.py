#!/usr/bin/python3
"""
Defines inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an inherited instance
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
