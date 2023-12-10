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
    @property
    def size(self):
        """Getting size of square"""
        return self.width
    @size.setter
    def size(self, value):
        """Setting the size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating square class"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
