#!/usr/bin/python3
"""Create a Square class"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize data, and check size"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter the size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Return position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter the position"""
        if type(value) is not tuple or len(value) is not 2 or \
                type(value[0]) is not int or type(value[1]) \
                is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of square"""
        return self.__size * self.__size

    def my_print(self):
        """Print with character (#) and spaces in position"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))
