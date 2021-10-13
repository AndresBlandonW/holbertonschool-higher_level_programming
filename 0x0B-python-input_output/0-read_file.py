#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """
    read content file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        read_data = f.read()
    for line in read_data:
        print(line, end='')
