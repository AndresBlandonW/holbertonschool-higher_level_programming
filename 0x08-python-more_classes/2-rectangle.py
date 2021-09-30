#!/usr/bin/python3
"""Creates class that defines a rectangle"""


class Rectangle:
    """Create a rectangle object"""
    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Return Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width and check errors"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height and check errors"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width != 0 or self.__width != 0:
            per = (2 * self.__height) + (2 * self.__width)
        else:
            per = 0
        return per
