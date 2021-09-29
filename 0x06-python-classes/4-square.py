#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialize data, and check size"""
        self.__size = size

    @property
    def size(self):
        """Return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter the size"""
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Return the area of square"""
        return self.__size * self.__size
