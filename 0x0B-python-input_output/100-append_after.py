#!/usr/bin/python3
"""Contains a function that appends to a file line after a stated string"""


def append_after(filename="", search_string="", new_string=""):
    """appends to a file line after a stated string"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.insert(i + 1, new_string)

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
