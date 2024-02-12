#!/usr/bin/python3
""" Class Rectangle inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """property to set it
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self, value):
        """property to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """property to set it"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property to retrieve it"""
        return self.__x

    @x.setter
    def x(self, value):
        """ property to set it """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property to retrieve it"""
        return self.__y

    @y.setter
    def y(self, value):
        """ property to set it """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area value of the Rectangle """
        return self.__height * self.__width

    def display(self):
        """ prints in stdout the shape """
        for _ in range(self.__y):
            print()
        gap = " " * self.__x
        char = "#" * self.__width
        for _ in range(self.__height):
            print(f"{gap}{char}")

    def __str__(self):
        """ Returns a string representation of a Rectangle instance. """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by adding the public method
        assigning an argument to each attribute:
        """
        length = len(args)
        if args is not None and length != 0:
            if length <= 5 and length > 0:
                attribute_names = ['id', 'width', 'height', 'x', 'y']

                for i in range(length):
                    setattr(self, attribute_names[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        my_dict = {
            'id': self.id, 'width': self.__width,
            'height': self.__height, 'x': self.__x, 'y': self.__y
            }
        return my_dict
