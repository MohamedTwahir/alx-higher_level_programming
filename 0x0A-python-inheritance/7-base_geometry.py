#!/usr/bin/python3
""" Creating BaseGeometry class """


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """
        area method for raising an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function for integer validation
        """
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than o".format(name))
