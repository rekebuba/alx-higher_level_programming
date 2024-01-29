#!/usr/bin/python3
"""
computes the area and the parameter of a givin height and width
"""


class Rectangle:
    """defines a Rectangle class"""
    def __init__(self, width=0, height=0):
        """initializing object attribute

        Args:
            width (int, optional): the value of the width. Defaults to 0.
            height (int, optional): the value of the height. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """property to retrieve it

        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """property to set it

        Args:
            value (int): the value passed

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve it

        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """property to set it

        Args:
            value (int): value passed

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
