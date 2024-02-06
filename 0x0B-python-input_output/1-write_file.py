#!/usr/bin/python3
""" writes a string to a text file """


def write_file(filename="", text=""):
    """ writes a string to a text file

    Returns:
        bite: bite read
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        number = file.write(text)
    return number
