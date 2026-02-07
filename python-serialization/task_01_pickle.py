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

    def display(self):
        """
        Method to print out the object's attributes.
        """
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """
        Method will take a filename as its parameter. Using the pickle module.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, EOFError):
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
        except (FileNotFoundError, EOFError):
            return
