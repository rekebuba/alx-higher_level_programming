#!/usr/bin/python3
"""
prints a text with 2 new lines after
each of these characters: . ? :
"""


def text_indentation(text):
    """function to modify the text

    Args:
        text (str): the text passed as a string

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        lines = text.split(delim)
        strip_line = ([line.strip(" ") for line in lines])
        text = (delim + "\n\n").join(strip_line)

    print("{}".format(text), end="")
