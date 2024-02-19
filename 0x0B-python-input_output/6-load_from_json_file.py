#!/usr/bin/python3
"""Contains a function that loads python objects from json files"""

import json


def load_from_json_file(filename):
    """loads python objects from json files"""
    with open(filename) as file:
        return json.load(file)
