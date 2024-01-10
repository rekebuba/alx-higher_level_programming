#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    arr = []
    for element in my_list:
        if element not in arr:
            add += element
            arr.append(element)
    return add
