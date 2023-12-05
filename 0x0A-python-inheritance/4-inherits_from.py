#!/usr/bin/python3
""" Return only subclass of a class """


def inherits_from(obj, a_class):
    """
    Function returning true if object is instance of class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
