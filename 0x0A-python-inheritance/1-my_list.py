#!/usr/bin/python3
"""This module contains a class MyList that inheritsf from 'list'"""

class MyList(list):
    """Custom list inheriting from python list"""
    def print_sorted(self):
        l = self.copy()
        l.sort()
        print(l)
        del l
