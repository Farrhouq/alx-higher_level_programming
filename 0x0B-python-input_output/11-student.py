#!/usr/bin/python3
"""Contains a Student class"""


class Student:
    """A Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {k: self.__dict__[k] for k in self.__dict__ if k in attrs}

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = value
