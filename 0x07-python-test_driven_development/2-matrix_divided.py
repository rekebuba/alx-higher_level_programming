#!/usr/bin/python3

def matrix_divided(matrix, div):
    new_matrix = [[]]
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i, part in enumerate(matrix):
        if len(part) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j, item in enumerate(part):
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            result = item / div
            new_matrix.append(result)
    return new_matrix
