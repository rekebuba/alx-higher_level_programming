#!/usr/bin/python
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return None
    add = 0
    arr = []
    for element in my_list:
        if element not in arr:
            add += element
            arr.append(element)
    return add
