#!/usr/bin/python3
""" prints My name followed by first and last name"""


def say_my_name(first_name, last_name=""):
    """provides the first and last name

    Args:
        first_name (string): passes their first name
        last_name (str, optional): passes last name. Defaults to "".

    Raises:
        TypeError: if the name passed is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
