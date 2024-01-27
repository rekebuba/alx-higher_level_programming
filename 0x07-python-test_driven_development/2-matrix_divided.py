#!/usr/bin/python3
"""matrix_divider"""

def matrix_divided(matrix, div):
    """divides a matrix by div

    Args:
        matrix (int or float)): contains numbers
        div (int): the value passed to as the divisor

    Raises:
        TypeError: if row is not list of list or if the items are not int or float
        ZeroDivisionError: when the divisor(div) is 0
        TypeError: each row of the matrix must have the same size

    Returns:
        int: a new matrix
    """
    if matrix is None:
        return [[]]

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        result = [round(item / div, 2) for item in row]
        new_matrix.append(result)

    return new_matrix
