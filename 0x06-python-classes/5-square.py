#!/usr/bin/python3
""" defines a class square """


class Square:
    """
    it defines a square by: (based on 4-square.py)
    """
    def __init__(self, size=0):
        """private instance attribute size
        Args:
            size (int, optional): the size to be squared. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """ initializing a getter and a setter

        Returns:
            _type_: self.__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ the setter part

        Args:
            value : the value passed

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area

        Returns:
            _type_: square value
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #:
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
