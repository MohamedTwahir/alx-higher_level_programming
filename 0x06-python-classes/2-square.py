#!/usr/bin/python3
"""Creation of square class"""


class Square:
    """Class square definition"""
    def __init__(self, size=0):
        """Initialization of the square class
        Args: size=0: size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
