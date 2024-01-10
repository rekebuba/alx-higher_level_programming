#!/usr/bin/python
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return None
    add = 0
    for element in my_list:
        if my_list.count(element) == 0:
            add += element
    return add
