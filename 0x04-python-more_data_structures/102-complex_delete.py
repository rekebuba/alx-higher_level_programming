#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dictionary = {}
    for key, val in a_dictionary.items():
        if val != value:
            new_dictionary[key] = val
    return new_dictionary
