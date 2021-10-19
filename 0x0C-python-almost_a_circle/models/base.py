#!/usr/bin/python3
"""Base Class"""


class Base:
    """The base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method"""
        if id is not None:
            self.id = int(id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
