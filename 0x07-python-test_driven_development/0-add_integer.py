#!/usr/bin/python3
""" to find the sum of two numbers """

def add_integer(a, b=98):
    """to find the sum of two numbers

    Args:
        a (int): integer type
        b (int, optional): integer type. Defaults to 98.

    Raises:
        TypeError: if a is not an integer or a float
        TypeError: if b is not an integer or a float

    Returns:
        int: the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    result = a + b

    return result
