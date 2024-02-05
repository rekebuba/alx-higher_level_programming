#!/usr/bin/python3
""" check if the object is an instance of a class """


def is_kind_of_class(obj, a_class):
    """check if the object is an instance of,
    or if the object is an instance of a class that inherited from
    the specified class

    Returns:
        bool: True if it is False otherwise
    """
    return isinstance(obj, a_class)
