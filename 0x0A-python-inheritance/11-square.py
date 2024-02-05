#!/usr/bin/python3
"""Module 11-Square.
Creates a Square class.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square.
    Private instance attribute size.
    Public method area().
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """Initializes a Square.
        Args:
            - size: size of the square
        """

        super().__init__(size, size)
