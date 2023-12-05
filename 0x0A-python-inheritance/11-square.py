#!/usr/bin/python3
""" Creating class Square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square inherited from class Rectanglee
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Area method/Function
        """
        return self.__size ** 2

    def __str__(self):
        """
        __str__ method/function
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
