"""
Unittest for the Rectangle Class.
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestForm(unittest.TestCase):
    """test case for Rectangle Class """

    def test_area(self):
        """ tests area """
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(120, 1).area(), 120)

    def test_error(self):
        """ tests errors """
        self.assertRaises(TypeError, lambda: Rectangle(120, "1"), msg="height must be an integer")
        self.assertRaises(TypeError, lambda: Rectangle("120", 1), msg="width must be an integer")
        self.assertRaises(TypeError, lambda: Rectangle(120, -2), msg="height must be > 0")
        self.assertRaises(TypeError, lambda: Rectangle(-120, -2), msg="width must be > 0")
        self.assertRaises(TypeError, lambda: Rectangle(120, 2, -2), msg="x must be >= 0")
        self.assertRaises(TypeError, lambda: Rectangle(120, 2, 2, -2), msg="y must be >= 0")
        self.assertRaises(TypeError, lambda: Rectangle(120, 1, "hi"), msg="x must be an integer")
        self.assertRaises(TypeError, lambda: Rectangle(120, 1, 5, "hi"), msg="y must be an integer")

    def test_display1(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Rectangle(4, 1).display()
            result = "####"
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, result)

    def test_display2(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Rectangle(6, 3).display()
            result = "######\n######\n######"
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, result)

    def test_str(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            print(Rectangle(4, 6, 2, 1, 12))
            result = "[Rectangle] (12) 2/1 - 4/6"
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, result)

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89)
            print(r1)

            r1.update(89, 2)
            print(r1)

            r1.update(89, 2, 3)
            print(r1)

            r1.update(89, 2, 3, 4)
            print(r1)

            r1.update(89, 2, 3, 4, 5)
            print(r1)

            result = "[Rectangle] (89) 10/10 - 10/10\n[Rectangle] (89) 10/10 - 2/10\n[Rectangle] (89) 10/10 - 2/3\n[Rectangle] (89) 4/10 - 2/3\n[Rectangle] (89) 4/5 - 2/3"
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, result)
