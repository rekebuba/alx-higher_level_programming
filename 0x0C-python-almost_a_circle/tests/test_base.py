"""
Unittest for the Base Class.
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestForm(unittest.TestCase):
    """test case for Rectangle Class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_to_json_string(self):
        """ test for JSON string representation """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)
        result = """[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]"""
        self.assertEqual(json_dictionary, result)

        r1 = Square(10, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)
        result = """[{"id": 2, "size": 10, "x": 2, "y": 8}]"""
        self.assertEqual(json_dictionary, result)

    def test_base_save_to_file(self):
        """ test JSON string representation saved to a file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as f:
            result = """[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]"""
            self.assertEqual(str(f.read()), result)

    def test_base_from_json_string(self):
        """ test """
