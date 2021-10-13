#!/usr/bin/python3
"""Student to JSON"""
import json


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """
        Defines a student by first name, last name, age
        """
        self.first_name = first_name
        self.laslast_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation"""
        return self.__dict__
