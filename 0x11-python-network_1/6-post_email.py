#!/usr/bin/python3
"""takes in a URL and an email address,
sends a POST request to the passed URL with
the email as a parameter, and finally displays
the body of the response.
"""
from requests import post
from sys import argv

if __name__ == "__main__":
    try:
        email = {'email': argv[2]}
        r = post(argv[1], data=email)
        print(r.text)
    except:
        pass