#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestsMax(unittest.TestCase):
    """class testsMax

    Args:
        unittest (module): inherits
    """
    def test_find_largest(self):
        """ a list of integer expected to return the max """
        value = [1, 2, 3]
        self.assertEqual(max_integer(value), 3)
    def test_empty_list(self):
        """ an empty list expected to return None """
        value = []
        self.assertEqual(max_integer(value), None)
    def test_invalid_list(self):
        """ giving invalid input should return TypeError """
        self.assertRaises(TypeError, max_integer, 1)
    def test_long_input(self):
        """ passing a very large number """
        value = [1000e1000, 10, 11]
        self.assertEqual(max_integer(value), 1000e1000)
    def test_negative_input(self):
        """ should return max when passing negative list """
        value = [-10, -1, -20]
        self.assertEqual(max_integer(value), -1)
    def test_float_input(self):
        """ should handle floating numbers """
        value = [1.2, 1.3, 4.5]
        self.assertEqual(max_integer(value), 4.5)
    def test_bool_input(self):
        value = [True, False]
        self.assertEqual(max_integer(value), True)
    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)
    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

if __name__ == '__main__':
    unittest.main()
