#!/usr/bin/python3
"""
11. Student to disk and reload
"""


class Student:
    """
    A class Student that defines a student by:

    Public instance attributes:
    first_name
    last_name
    age
    """
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        representation of a Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            res = {}
            for i in attrs:
                if i in self.__dict__:
                    res[i] = self.__dict__[i]
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """
        Public method that replaces all attributes of the Student instance.
        """
        self.__dict__.update(json)
