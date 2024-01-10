#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    max_score = float('-inf')
    max_key = None

    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            max_key = key

    return max_key
