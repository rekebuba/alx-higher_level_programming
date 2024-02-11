#!usr/bin/python3
""" Class Square inherits from Rectangle """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class describing a square inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a Square instance """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """property to retrieve it"""
        return self.__width

    @size.setter
    def size(self, value):
        """property to set it
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """Returns a string representation of a Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.__width}"

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by adding the public method
        assigning an argument to each attribute:
        """
        length = len(args)
        if length == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            if length > 5:
                raise IndexError("tuple index out of range")

            attribute_names = ['id', 'size', 'x', 'y']

            for i in range(length):
                setattr(self, attribute_names[i], args[i])

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        my_dict = {
            'id': self.id, 'size': self.__width,
            'x': self.x, 'y': self.y
            }
        return my_dict
