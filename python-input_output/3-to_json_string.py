#!/usr/bin/python3
"""
3. To JSON string
"""
from json import dumps


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)
    """
    return dumps(my_obj)
