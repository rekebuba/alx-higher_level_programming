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

    def __str__(self):
        """Returns a string representation of a Square instance."""
        return f"[Square] ({self.id}) ({self.x})/({self.y}) - {self.width}"
