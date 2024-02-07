#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle
    """
    my_list = []
    if n <= 0:
        return my_list

    sub_list = [1]
    my_list.append(sub_list)

    for i in range(1, n):
        prev_row = my_list[i - 1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        my_list.append(current_row)

    return my_list
