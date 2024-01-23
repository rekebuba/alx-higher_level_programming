#!/usr/bin/python3
""" define a class square """


class Square:
    """
    it defines a square by: (based on 2-square.py)
    """
    def __init__(self, size=0):
        """private instance attribute size

        Args:
            size (int, optional): the size to be squared. Defaults to 0.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area

        Returns:
            _type_: square value
        """
        return self.__size ** 2
