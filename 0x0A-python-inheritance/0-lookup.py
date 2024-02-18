#!/usr/bin/python3
""" This is the lookup function that prints all available methods and
classes for an object """


def lookup(obj):
    """This function prints all available methods and classes for
    an object """
    return dir(obj)
