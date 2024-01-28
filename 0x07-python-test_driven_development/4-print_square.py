#!/usr/bin/python3
"""
print a square with # character
"""
def print_square(size):
    """a function to print the square

    Args:
        size (int): the size passed to print square

    Raises:
        TypeError: if the size is boolean
        TypeError: it the size is not integer or a float
        ValueError: if the size is < 0
    """
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#' * size)
