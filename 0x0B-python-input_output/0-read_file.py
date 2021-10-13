#!/usr/bin/python3
"""function that reads a text file"""

def read_file(filename=""):
    with open(filename) as f:
        read_data = f.read()
    for line in read_data:
        print(line, end='')
