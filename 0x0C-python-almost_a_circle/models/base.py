#!/usr/bin/python3
""" Class Base """

class Base:
    """
    To manage id attribute in all the future classes
    and to avoid duplicating the same code.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        constructor
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
