#!/usr/bin/python3
"""A function for adding two integers."""


def add_integer(a, b=98):
    """A function returning int(a) + int(b)."""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
