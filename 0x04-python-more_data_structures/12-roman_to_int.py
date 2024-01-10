#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prv = 0
    for char in reversed(roman_string):
        result = dictionary.get(char)
        if result < prv:
            total -= result
        else:
            total += result
            prv = result
    return total
