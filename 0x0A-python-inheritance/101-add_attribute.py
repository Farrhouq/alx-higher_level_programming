#!/usr/bin/python3
"""contains a function that adds a new attribute to an object
if it's possible"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object if it's possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
