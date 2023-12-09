#!/usr/bin/python3
"""A Base class"""


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
