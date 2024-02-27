#!/usr/bin/python3
"""Contains a class Base"""

import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary()
                                           for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries represented by json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Creating a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)      # Creating a dummy Square instance
        else:
            return None

        # Updating the dummy instance with real values
        dummy_instance.update(**dictionary)
        return dummy_instance
