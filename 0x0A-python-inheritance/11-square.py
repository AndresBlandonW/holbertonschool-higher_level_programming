#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size):
        """
        Init method for Square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return area of REctangle object"""
        return self.__size * self.__size

    def __str__(self):
        """Print description of Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
