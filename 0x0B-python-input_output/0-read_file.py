#!/usr/bin/python3
"""Contains a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename)as file:
        print(file.read())
