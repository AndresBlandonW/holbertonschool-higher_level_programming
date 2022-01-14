#!/usr/bin/python3
"""takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter
as a parameter.
"""
from request import get, post
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    dict = {}
    if len(argv) < 2:
        dict = {'q': ''}
    else:
        dict = {'q': argv[1]}

    r = post(url, data=dict)
    try:
        if r.json() == {}:
            print('No result')
        else:
            print('[{}] {}'.format(r.json()['id'], r.json()['name']))
    except:
        print('Not a valid JSON')
