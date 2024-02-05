#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """class MyList

    Args:
        list (class): class
    """
    def print_sorted(self):
        """
        print_sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
