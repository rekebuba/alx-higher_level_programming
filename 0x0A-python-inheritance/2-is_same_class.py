#!/usr/bin/python3
""" check the instance of a class """


def is_same_class(obj, a_class):
    """check the instance

    Returns:
        bool: True if it is instance of the specified class
        otherwise False
    """
    return type(obj) is a_class
