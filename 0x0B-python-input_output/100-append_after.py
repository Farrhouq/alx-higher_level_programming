#!/usr/bin/python3
"""Contains a function that appends to a file line after a stated string"""


def append_after(filename="", search_string="", new_string=""):
    """appends to a file line after a stated string"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        if search_string in lines[i]:
            lines.insert(i + 1, f"{new_string}")
            i += 1
        i += 1


    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
