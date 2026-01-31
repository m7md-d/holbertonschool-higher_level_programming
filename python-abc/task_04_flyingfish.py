#!/usr/bin/python3
"""
Module demonstrating multiple inheritance and Method Resolution Order (MRO).
"""


class Fish:
    """
    Class representing a fish.
    """
    def swim(self):
        """Swiming fish!"""
        print("The fish is swimming")

    def habitat(self):
        """Fish in the water"""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""
    def fly(self):
        """Flying fly"""
        print("The bird is flying")

    def habitat(self):
        """Fly in the sky"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish that inherits from both Fish and Bird.
    Demonstrates multiple inheritance.
    """

    def fly(self):
        """Overrides the fly method from Bird."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides the swim method from Fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides the habitat method from both parents."""
        print("The flying fish lives both in water and the sky!")
