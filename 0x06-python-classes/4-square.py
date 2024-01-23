#!/usr/bin/python3
""" defines a class square """


class Square:
    
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
            _type_: self
        """
        return self.__size
    @size.setter
    def size(self, value):
        """ the getter part

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
