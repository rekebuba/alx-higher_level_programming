#!/usr/bin/python3
""" multiply two matrix """


def matrix_mul(m_a, m_b):
    """ multiply two matrix

    Args:
        m_a (matrix): the first matrix
        m_b (matrix): the second matrix

    Raises:
        TypeError: if either is not a list
        TypeError: if either is not a list of list
        ValueError: if either is empty
        TypeError: if not the same size
        ValueError: if the matrixes can not be multiplied

    Returns:
        int: a new matrix
    """
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be b list")

    if not any(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not any(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be b list of lists")


    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError("m_a should contain only integers or floats")
    row_m_b = 0
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError("m_b should contain only integers or floats")
        row_m_b += 1

    if len(m_a[0]) != row_m_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for row in m_a:
        row_result = []
        for i in range(len(m_b[0])):
            add = sum(int(row[j]) * int(m_b[j][i]) for j in range(len(row)))
            row_result.append(add)
        result.append(row_result)
    return result
