#!/usr/bin/python3
"""
This is the module defines a function that adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int): the first number
        b (int): the second number

    Returns:
        the sum of the two integers
    
    Raises:
        TypeError if either number is not int-ible
    """
    try:
        a = int(a)
    except:
        raise TypeError("a must be an integer") from None
    try:
        b = int(b)
    except:
        raise TypeError("b must be an integer") from None
    
    return a + b
