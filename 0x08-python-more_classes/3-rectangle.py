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

    def __str__(self):
        """prints a rectangle with '#' character

        Returns:
            str: #
        """
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        for i in range(self.__height):
            result += "#" * self.__width
            if i != self.__height - 1:
                result += "\n"
        return result

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

    def area(self):
        """computes the area of a rectangle

        Returns:
            int: the value of the area
        """
        return self.__height * self.__width

    def perimeter(self):
        """computes the perimeter of a rectangle

        Returns:
            int: the perimeter of a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__height) + 2*(self.__width)
