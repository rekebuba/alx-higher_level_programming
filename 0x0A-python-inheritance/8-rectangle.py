#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    Private instance attributes:
        - width
        - height
    Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """Initializes an instance.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator(width, height)
        self.__width = width
        self.__height = height
