#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    arr = []
    for element in set_1:
        if element not in set_2:
            arr.append(element)
    for element in set_2:
        if element not in set_1:
            arr.append(element)
    return arr
