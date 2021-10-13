#!/usr/bin/python3
"""Geometry module"""


class BaseGeometry:
    """Write an empty class"""
    pass

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
            raise ValueError("{} must be greater than 0".format(name))
