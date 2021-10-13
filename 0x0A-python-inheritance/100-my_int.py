#!/usr/bin/python3
"""Class Square that inherits from Rectangle"""


class MyInt(int):
    def __eq__(self, value):
        """Redefine equality to be unequal"""
        return self.value == value.value

    def __ne__(self, value):
        """Delega el resultado"""
        return not self == value
