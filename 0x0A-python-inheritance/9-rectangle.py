#!/usr/bin/python3
"""Class Rectangle for base geometry"""


class BaseGeometry:
    """Class for base geometry"""
    def area(self):
        """
        Not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Check is integer

        Return - validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be an integer".format(name))

"""Class for Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Class for Rectangel inherits from BaseGeometry"""
    def __init__(self, width, height):
        """
        Init method for Rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Return area of REctangle object"""
        return self.__width * self.__height

    def __str__(self):
        """Print description of Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
