#!/usr/bin/python3
"""
6. Create object from a JSON file
"""
from json import load


def load_from_json_file(filename):
    """
    function that creates an Object from a "JSON file"
    """
    with open(filename, "r", encoding="utf-8") as f:
        return load(f)
