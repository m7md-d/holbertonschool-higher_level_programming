#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    TestCase class for max_integer function
    """

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test with a list where the max value is the first element"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_one_element_list(self):
        """Test with a list containing only one integer"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test with a list of floats"""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test with a list of mixed integers and floats"""
        mixed = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(mixed), 15.5)

    def test_string(self):
        """Test with a string"""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test with a list of strings"""
        strings = ["Brennan", "by", "Holberton"]
        self.assertEqual(max_integer(strings), "by")

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertIsNone(max_integer(""))

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        negatives = [-1, -5, -3, -4]
        self.assertEqual(max_integer(negatives), -1)


if __name__ == '__main__':
    unittest.main()
