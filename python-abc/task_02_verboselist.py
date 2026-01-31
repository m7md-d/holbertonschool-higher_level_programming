#!/usr/bin/python3
"""
Module defining VerboseList class that extends the built-in list.
"""


class VerboseList(list):
    """
    A list that prints notifications when modified.
    """
    def append(self, item):
        """
        Print a message after adding an item to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Print a message after extending the list.
        """
        item_count = len(items)
        super().extend(items)
        print(f"xtended the list with [{item_count}] items.")

    def remove(self, item):
        """
        Print a message before removing the item from the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Print a message before popping the item from the list.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
