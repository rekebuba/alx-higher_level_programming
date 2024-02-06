#!/usr/bin/python3
""" appends a string at the end of a text file """


def append_write(filename="", text=""):
    """appends a string at the end of a text file

    Returns:
        bite: bite read
    """
    with open(filename, mode="a+", encoding="utf-8") as file:
        return file.write(text)
