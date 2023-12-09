#!/usr/bin/python3
"""Creating a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Initialization"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if vlaue <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x value of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y value of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y coordinates of the rectangle setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method to calculate area of rectangle"""
        return self.width * self.height
