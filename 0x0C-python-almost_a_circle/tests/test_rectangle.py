"""
Unittest for the Rectangle Class.
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

    def test_rectangle_id(self):
        """Test Rectangle class: check for id."""

        r0 = Rectangle(1, 2)
        self.assertEqual(r0.id, 1)
        r = Rectangle(2, 3)
        self.assertEqual(r.id, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 3)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2, 4, 5, 34)
        self.assertEqual(r4.id, 34)
        r5 = Rectangle(10, 2, 4, 5, -5)
        self.assertEqual(r5.id, -5)
        r6 = Rectangle(10, 2, 4, 5, 9)
        self.assertEqual(r6.id, 9)

    def test_rectangle_area(self):
        """ tests area """
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(120, 1).area(), 120)

    def test_rectangle_error(self):
        """ tests errors """
        self.assertRaises(TypeError, lambda: Rectangle(120, "1"), msg="height must be an integer")
        self.assertRaises(TypeError, lambda: Rectangle("120", 1), msg="width must be an integer")
        self.assertRaises(ValueError, lambda: Rectangle(120, -2), msg="height must be > 0")
        self.assertRaises(ValueError, lambda: Rectangle(-120, -2), msg="width must be > 0")
        self.assertRaises(ValueError, lambda: Rectangle(120, 2, -2), msg="x must be >= 0")
        self.assertRaises(ValueError, lambda: Rectangle(120, 2, 2, -2), msg="y must be >= 0")
        self.assertRaises(TypeError, lambda: Rectangle(120, 1, "hi"), msg="x must be an integer")
        self.assertRaises(TypeError, lambda: Rectangle(120, 1, 5, "hi"), msg="y must be an integer")

    def test_rectangle_display1(self):
        """ test for correct output printed in stdio """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Rectangle(4, 1).display()
            result = "####"
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, result)

    def test_rectangle_display2(self):
        """ test for correct output printed in stdio """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Rectangle(6, 3).display()
            result = "######\n######\n######"
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, result)

    def test_rectangle_str(self):
        """ test for string representation of rectangle """
        r = Rectangle(4, 6, 2, 1, 12)
        result = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), result)

        r = Rectangle(5, 5, 1)
        result = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str(r), result)

        r = Rectangle(7, 1, 8, 9, 10)
        result = "[Rectangle] (10) 8/9 - 7/1"
        self.assertEqual(str(r), result)

    def test_rectangle_update(self):
        """ test for the update method for rectangle using *arg"""
        r = Rectangle(10, 10, 10, 10)
        result = "[Rectangle] (1) 10/10 - 10/10"
        self.assertEqual(str(r), result)

        r.update(89)
        result = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(str(r), result)

        r.update(89, 2)
        result = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(str(r), result)

        r.update(89, 2, 3)
        result = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(str(r), result)

        r.update(89, 2, 3, 4)
        result = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(str(r), result)

        r.update(89, 2, 3, 4, 5)
        result = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(str(r), result)

    def test_rectangle_update2(self):
        """ test for the update method for square using **kwarg"""
        r = Rectangle(10, 10, 10, 10)
        result = "[Rectangle] (1) 10/10 - 10/10"
        self.assertEqual(str(r), result)

        r.update(height=1)
        result = "[Rectangle] (1) 10/10 - 10/1"
        self.assertEqual(str(r), result)

        r.update(width=1, x=2)
        result = "[Rectangle] (1) 2/10 - 1/1"
        self.assertEqual(str(r), result)

        r.update(y=1, width=2, x=3, id=89)
        result = "[Rectangle] (89) 3/1 - 2/1"
        self.assertEqual(str(r), result)

        r.update(x=1, height=2, y=3, width=4)
        result = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(str(r), result)

    def test_rectangle_to_dictionary(self):
        r = Rectangle(2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r.update(**r_dict)
        result = "[Rectangle] (1) 4/5 - 2/3"
        self.assertEqual(str(r), result)

        r = Rectangle(10, 2, 1, 9)
        r_dict = r.to_dictionary()
        r.update(**r_dict)
        result = "[Rectangle] (2) 1/9 - 10/2"
        self.assertEqual(str(r), result)
