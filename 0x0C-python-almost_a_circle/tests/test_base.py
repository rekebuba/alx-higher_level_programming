"""
Unittest for the Base Class.
"""

import unittest
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
        """ test return value of JSON string representation"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        result = [{'id': 89, 'width': 10, 'height': 4}, {'id': 7, 'width': 1, 'height': 7}]
        self.assertEqual(list_output, result)
        self.assertIsInstance(list_output, list)

    def test_base_create(self):
        """ test for attributes of the new instance created """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)

    def test_base_load_from_file(self):
        """ test the returned value """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        result = ["[Rectangle] (1) 2/8 - 10/7", "[Rectangle] (2) 0/0 - 2/4"]
        r_id = []
        for i, rect in enumerate(list_rectangles_input):
            r_id.append(id(rect))
            self.assertEqual(str(rect), result[i])

        for i, rect in enumerate(list_rectangles_output):
            self.assertEqual(str(rect), result[i])
            self.assertNotEqual(id(rect), r_id[i])

    def test_base_save_to_file_csv(self):
        """ test if correctly saved to CSV file """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()


        result = ["[Rectangle] (1) 2/8 - 10/7", "[Rectangle] (2) 0/0 - 2/4"]
        r_id = []
        for i, rect in enumerate(list_rectangles_input):
            r_id.append(id(rect))
            self.assertEqual(str(rect), result[i])

        for i, rect in enumerate(list_rectangles_output):
            self.assertEqual(str(rect), result[i])
            self.assertNotEqual(id(rect), r_id[i])

if __name__ == '__main__':
    unittest.main()
