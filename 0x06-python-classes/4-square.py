#!/usr/bin/python3
"""Creation of square class"""


class Square:
    """Class square definition"""
    def __init__(self, size=0):
        """Initializing a sqaure class
        Args: size=0: size of square
        """
        self.__size = size

    @property
    def size(self):
        """ Getting the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setting the size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculating the area of the square """
        return (self.__size ** 2)
