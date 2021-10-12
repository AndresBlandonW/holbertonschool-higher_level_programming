#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance
    of the specified class

    Return - True or False
    """
    return type(obj) is a_class
