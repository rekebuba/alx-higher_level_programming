#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return None

    row = [[square(x) for x in y] for y in matrix]

    return row


def square(x):
    return x ** 2
