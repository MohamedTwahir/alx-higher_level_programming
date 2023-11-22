#!/usr/bin/python3
"""Creation of square class"""


class Square:
    """Class square definition"""
    def __init__(self, size=0):
        """Initializing a square class
        Args: size=0: size of square
        """
        self.__size = size

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculating the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints a square with #,
        at position given by position attribute.
        """
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        for j in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for y in range(0, self.__size):
                print("#", end="")
            print()
