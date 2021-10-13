#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """
        Defines a student by first name, last name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if type(attrs) is list and all(isinstance(i, str) for i in attrs):
            new_dict = {}
            for k in list(self.__dict__.keys()):
                if k in attrs:
                    new_dict[k] = self.__dict__[k]
            return new_dict

        return self.__dict__
