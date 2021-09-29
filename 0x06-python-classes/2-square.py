#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialize a size and check data"""
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
