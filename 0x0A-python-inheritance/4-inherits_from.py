#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class

    Return - True or False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
