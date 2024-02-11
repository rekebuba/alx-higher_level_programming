"""
Unittest for the Square Class.
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from models.square import Square
from models.base import Base


class TestForm(unittest.TestCase):
    """test case for Square Class """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_area(self):
        """ tests area """
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)

    def test_square_error(self):
        """ tests errors """
        self.assertRaises(TypeError, lambda: Square("120", 1), msg="width must be an integer")
        self.assertRaises(ValueError, lambda: Square(-120, -2), msg="width must be > 0")
        self.assertRaises(ValueError, lambda: Square(120, -2), msg="x must be >= 0")
        self.assertRaises(ValueError, lambda: Square(120, 2, -2), msg="y must be >= 0")
        self.assertRaises(TypeError, lambda: Square(120, "hi"), msg="x must be an integer")
        self.assertRaises(TypeError, lambda: Square(120, 5, "hi"), msg="y must be an integer")

    def test_square_display1(self):
        """ test output """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Square(3).display()
            result = "###\n###\n###"
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, result)

    def test_square_display2(self):
        """ test output """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Square(3, 1).display()
            result = "###\n ###\n ###"
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, result)

    def test_square_str(self):
        """ test string representation """
        r = Square(4)
        result = "[Square] (1) 0/0 - 4"
        self.assertEqual(str(r), result)

        r = Square(5, 1)
        result = "[Square] (2) 1/0 - 5"
        self.assertEqual(str(r), result)

        r = Square(5, 1, 2)
        result = "[Square] (3) 1/2 - 5"
        self.assertEqual(str(r), result)

    def test_square_update1(self):
        """ test for the update method for square using *arg"""
        r = Square(5)
        result = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(r), result)

        r.update(10)
        result = "[Square] (10) 0/0 - 5"
        self.assertEqual(str(r), result)

        r.update(1, 2)
        result = "[Square] (1) 0/0 - 2"
        self.assertEqual(str(r), result)

        r.update(1, 2, 3)
        result = "[Square] (1) 3/0 - 2"
        self.assertEqual(str(r), result)

        r.update(1, 2, 3, 4)
        result = "[Square] (1) 3/4 - 2"
        self.assertEqual(str(r), result)

    def test_square_update2(self):
        """ test for the update method for square using **kwarg"""
        r = Square(5)
        r.update(x=12)
        result = "[Square] (1) 12/0 - 5"
        self.assertEqual(str(r), result)
        
        r.update(size=7, y=1)
        result = "[Square] (1) 12/1 - 7"
        self.assertEqual(str(r), result)
        
        r.update(size=7, id=89, y=1)
        result = "[Square] (89) 12/1 - 7"
        self.assertEqual(str(r), result)

    def test_square_to_dictionary(self):
        """ test dictionary method for square """
        r = Square(10, 2, 1)
        r_dict = r.to_dictionary()
        r.update(**r_dict)
        result = "[Square] (1) 2/1 - 10"
        self.assertEqual(str(r), result)

        r = Square(1, 1)
        r_dict = r.to_dictionary()
        r.update(**r_dict)
        result = "[Square] (2) 1/0 - 1"
        self.assertEqual(str(r), result)
