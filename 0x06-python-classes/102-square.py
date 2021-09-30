#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialize data, and check size"""
        self.size = size

    @property
    def size(self):
        """Return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """Return the area of square"""
        return self.__size * self.__size

    def __lt__(self, other):
        """Compare less than"""
        return self.size < other.size

    def __le__(self, other):
        """Compare less than or equal"""
        return self.size <= other.size

    def __eq__(self, other):
        """Compare is equal"""
        return self.size == other.size

    def __ne__(self, other):
        """Compare is not equal"""
        return self.size != other.size

    def __gt__(self, other):
        """Compare is greater than"""
        return self.size > other.size

    def __ge__(self, other):
        """Compare greater than or equal"""
        return self.size >= other.size
