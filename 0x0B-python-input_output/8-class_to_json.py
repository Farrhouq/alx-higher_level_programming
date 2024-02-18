#!/usr/bin/python3
"""Contains a function that serializes a class into dict"""

import json


def class_to_json(obj):
    """serializes a class into dict"""
    return obj.__dict__
