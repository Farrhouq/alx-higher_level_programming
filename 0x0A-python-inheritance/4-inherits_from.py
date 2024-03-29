#!/usr/bin/python3
"""Contains a function that returns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified class ;
otherwise False."""


def inherits_from(obj, a_class):
    """eturns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified class ;
otherwise False."""
    return issubclass(type(obj), a_class) and not type(obj) is a_class
