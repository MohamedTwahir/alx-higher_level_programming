#!/usr/bin/python3
""" Function that return True if object is an instance of """


def is_kind_of_class(obj, a_class):
    """
    Returns True is the object is an instance of

    Args:
    - obj: Any object
    - a_class: Class or tuple of classess
    """
    return isinstance(obj, a_class)
