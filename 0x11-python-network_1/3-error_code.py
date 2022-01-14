#!/usr/bin/python3
"""Takes in a URL, send a request to the URL
and displays the body of the response"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        reqs = Request(url)

        with urlopen(reqs) as response:
            read = response.read()
            print(read.decode("UTF-8"))
    except HTTPError as e:
        e = str(e)
        e = e.split()[2].replace(':', '')
        print('Error code: {}'.format(e))
