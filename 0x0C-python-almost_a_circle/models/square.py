#!/usr/bin/python3
"""Creating class square that inherits from class rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Inherited from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading string method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
