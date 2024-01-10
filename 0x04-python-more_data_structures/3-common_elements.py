#!/usr/bin/python
def common_elements(set_1, set_2):
    arr = []
    for element in set_1:
        if element in set_2:
            arr.append(element)
    return arr
