#!/usr/bin/python3
""" defines a class square """


class Square:
    """
    it defines a square by: (based on 5-square.py)
    """

    def __init__(self, size=0, position=(0, 0)):
        """private instance attribute size
        Args:
            size (int, optional): the size to be squared. Defaults to 0.
        """

        self.size = size
        self.position = position

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

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of a square

        Returns:
            area
        """

        return self.__size * self.__size

    @property
    def position(self):
        """ initializing a getter and a setter

        Returns:
            _type_: self.position__position
        """

        return self.__position

    @position.setter
    def position(self, value):
        """ the setter part

        Args:
            value : the value passed as a tuple

        Raises:
            TypeError: checks if it is a tuple
            and every tuple is an integer
        """

        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print("")
        else:
            for line in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
