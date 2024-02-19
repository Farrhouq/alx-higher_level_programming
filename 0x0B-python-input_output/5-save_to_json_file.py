#!/usr/bin/python3
"""Contains a function that writes an object to a file in json"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file in json"""
    with open(filename, 'w') as file:
        return json.dump(my_obj, file)
