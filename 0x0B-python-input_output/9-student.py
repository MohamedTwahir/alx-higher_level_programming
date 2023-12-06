#!/usr/bin/python3
"""Creating a class Student"""


class Student:
    """Class Definition"""
    def __init__(self, first_name, last_name, age):
        """ Initializing """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method to retrieve dictionary representation
        """
        return self.__dict__
