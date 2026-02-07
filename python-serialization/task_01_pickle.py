#!/usr/bin/python3
"""
1. Pickling Custom Classes
"""
import pickle


class CustomObject:
    """
    Custom object class.
    """
    def __init__(self, name, age, is_student):
        """
        initialize class elements
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        Method will take a filename as its parameter. Using the pickle module.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return

    @classmethod
    def deserialize(cls, filename):
        """
        Class method will take a filename as its parameter.
        Using the pickle module.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return
