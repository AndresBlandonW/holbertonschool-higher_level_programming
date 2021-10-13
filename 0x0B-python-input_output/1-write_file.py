#!/usr/bin/python3
"""function that write a text file"""


def write_file(filename="", text=""):
    """
    Write in file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
