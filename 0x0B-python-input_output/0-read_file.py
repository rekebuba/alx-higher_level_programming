#!usr/bin/python3
""" read the entire file """


def read_file(filename=""):
    """a function to read the file
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
