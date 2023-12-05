#!/usr/bin/python3
""" Creating class Square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square inheriting from rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Function for area
        """
        return self.__size ** 2
