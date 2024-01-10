#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    arr = []
    denom = 0

    for i, j in my_list:
        arr.append(i * j)
        denom += j

    avg = sum(arr) / denom
    return avg
