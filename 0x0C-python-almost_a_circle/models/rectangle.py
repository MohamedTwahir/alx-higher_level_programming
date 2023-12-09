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
        self.__width = value

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """x value of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the x value"""
        self.__x = value

    @property
    def y(self):
        """Y value of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y coordinates of the rectangle setter"""
        self.__y = value
