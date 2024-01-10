#!/usr/bin/python3
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return None

    total = 0
    last_values = 0

    for i in my_list:
        total += add_tuple(i)

    for j in my_list:
        last_values += j[1]

    average = total / last_values
    return average


def add_tuple(x):
    return x[0] * x[1]
