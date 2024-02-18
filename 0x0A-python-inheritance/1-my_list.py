#!/usr/bin/python3
"""This module contains a class MyList that inheritsf from 'list'"""


class MyList(list):
    """Custom list inheriting from python list"""

    def print_sorted(self):
        list_copy = self.copy()
        list_copy.sort()
        print(list_copy)
        del list_copy
