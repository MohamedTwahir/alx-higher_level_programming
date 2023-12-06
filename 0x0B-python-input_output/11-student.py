#!/usr/bin/python3
"""Creating a class Student"""


class Student:
    """Class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """
        method to initialize the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method to retrieve a dict representation of student
        """
        if (type(attrs)) == list and all(type(i) == str for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """updates for student attributes"""
        for i in json:
            self.__dict__.update({i: json[i]})
