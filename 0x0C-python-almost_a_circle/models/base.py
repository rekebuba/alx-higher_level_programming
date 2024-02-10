#!/usr/bin/python3
""" Class Base """
import json
import os

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
        """ writes the JSON string representation of list_objs to a file """
        my_list = []
        if list_objs is None:
            return my_list
        my_list = cls.to_json_string([list_obj.to_dictionary() for list_obj in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
                file.write(my_list)
        return my_list

    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ a Class method that returns a list of instances """
        result = []
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                my_lists = cls.from_json_string(file.read())
                for my_list in my_lists:
                    result.append(cls.create(**my_list))
        return result
