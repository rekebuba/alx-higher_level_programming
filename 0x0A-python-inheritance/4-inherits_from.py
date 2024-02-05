#!/usr/bin/python3
""" check if the object is instance of a class """


def inherits_from(obj, a_class):
    """check if the object is directly or indirectly inherited

    Returns:
        bool: True if it an instance or False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
