#!/usr/bin/python3

def matrix_divided(matrix, div):
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list \
                of lists) of integers/floats")
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError("matrix must be a matrix (list of \
                lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        result = [round(item / div, 2) for item in row]
        new_matrix.append(result)
    return new_matrix
