#!/usr/bin/python3
"""add new attribute"""


def add_attribute(obj, name, value):
    """"dds a new attribute to an object if s possible"""
    if hasattr(obj, '__dict__'):
            setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
