#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is the instance of,
    or if the object is an instance of a class
    that inherited from

    Return - True or False
    """
    if isinstance(obj, a_class) or issubclass(type(obj), type(a_class)):
        return True

    return False
