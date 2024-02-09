#!/usr/bin/python3
""" Class Base """
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (not isinstance(list_dictionaries, list) or
            not all(isinstance(x, dict) for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        my_list = []
        if list_objs is None:
            return my_list
        my_list = cls.to_json_string([list_obj.to_dictionary() for list_obj in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
                file.write(my_list)
        return my_list
