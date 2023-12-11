#!/usr/bin/python3
"""A Base class"""

import json
import os


class Base:
    """Defining the Class Created"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class Initialization"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes json representation string to a file"""
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"

        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """method that returns string from json(decoding)"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creating an instance of class Base"""
        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance
