#!/usr/bin/python3
"""
a function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object:
"""


def class_to_json(obj):
    """
    JSON serialization for a class
    """
    serializable_attributes = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value

    return serializable_attributes
