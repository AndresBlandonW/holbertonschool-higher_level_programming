#!/usr/bin/python3
"""Creates class that defines a rectangle"""


class Rectangle:
    """Create a rectangle object"""
    def __init__(self, width=0, height=0):
        """init rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width and check errors"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height and check errors"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Print the rectangle using (#)"""
        if self.__width == 0 or self.__height == 0:
            return ""

        string = ""
        for i in range(self.__height):
            string += ("#" * self.__width)
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """String representation"""
        return f'Rectangle({self.__width}, {self.__height})'
