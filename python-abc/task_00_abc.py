#!/usr/bin/python3
"""
This module defines an abstract base class Animal and its subclasses
Dog and Cat to demonstrate abstraction and polymorphism.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses
        to return the sound of the animal.
        """
        pass

class Dog(Animal):
    """
    Class representing a Dog, inheriting from Animal.
    """

    def sound(self):
        """
        Implementation of sound method for Dog.
        Returns:
            str: "Bark"
        """
        return "Bark"

class Cat(Animal):
    """
    Class representing a Cat, inheriting from Animal.
    """

    def sound(self):
        """
        Implementation of sound method for Cat.
        Returns:
            str: "Meow"
        """
        return "Meow"
