#!/usr/bin/python3
"""
Module demonstrating Mixins in Python through a Dragon class.
"""


class SwimMixin:
    """Provides swimming functionality."""
    def swim(self):
        """Dragon swim"""
        print("The creature swims!")


class FlyMixin:
    """Provides flying functionality."""
    def fly(self):
        """Dragon fly"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that combines swimming and flying abilities
    using Mixins, plus its own unique abilities.
    """
    def roar(self):
        """Prints the dragon's unique roar."""
        print("The dragon roars!")
