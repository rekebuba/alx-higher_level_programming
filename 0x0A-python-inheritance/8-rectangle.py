#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation 

        Args:
            width (int): _description_
            height (int): _description_
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, self.__width, self.__height)
