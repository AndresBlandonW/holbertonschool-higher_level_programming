#!/usr/bin/python3
"""takes in a URL, send a request to URL
and displays the value of the variable"""
from requests import get
from sys import argv

if __name__ == "__main__":
    print(get(argv[1]).headers.get('x-request-id'))
