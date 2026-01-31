#!/usr/bin/python3
"""
Module for CountedIterator class.
This class wraps an iterator and keeps track of the number of items iterated.
"""


class CountedIterator:
    """
    An iterator wrapper that counts how many items have been fetched.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator and the counter.

        Args:
            iterable: Any object that can be iterated (list, tuple, etc.)
        """
        self.iterable = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Returns the current number of items iterated.
        """
        return self.counter

    def __next__(self):
        """
        Fetches the next item and increments the counter.

        Raises:
            StopIteration: If there are no more items to fetch.
        """
        item = next(self.iterable)
        self.counter += 1
        return item

    def __item__(self):
        """
        Returns the iterator object itself.
        """
        return self
