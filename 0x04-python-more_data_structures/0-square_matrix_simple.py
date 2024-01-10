#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return None

    square = lambda x: x ** 2
    row = [[square(x) for x in y] for y in matrix]

    return row
