#!/usr/bin/python3
"""Contains function that checks a class against some"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class"""
    return type(obj) is a_class
