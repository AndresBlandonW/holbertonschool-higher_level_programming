#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""


class MyInt(int):
    def __eq__(self, value):
        """Redefine equality to be unequal"""
        if isinstance(type(value), type(self)):
            return self == value
        return False

    def __ne__(self, value):
        """Delegate the result"""
        return not self.__eq__(value)
