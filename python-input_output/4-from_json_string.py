#!/usr/bin/python3
"""
4. From JSON string to Object
"""
from json import loads


def from_json_string(my_str):
    """
    Function that returns an object represented by a JSON string.
    """
    return loads(my_str)
