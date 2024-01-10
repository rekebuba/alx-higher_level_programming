#!/usr/bin/python
def only_diff_elements(set_1, set_2):
    arr = []
    for element in set_1:
        if element not in arr:
            arr.append(element)
    for element in set_2:
        if element not in arr:
            arr.append(element)
    return arr
