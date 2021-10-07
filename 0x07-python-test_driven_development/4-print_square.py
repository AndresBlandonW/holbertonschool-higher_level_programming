#!/usr/bin/python3
"""Function that prints a square with the character #"""


def print_square(size):
    """
    check the values of size,
    size >= 0

    Return - square with #
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        print("#" * size)
