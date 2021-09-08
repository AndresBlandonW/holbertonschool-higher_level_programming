#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = str
    for i in range(0, len(str)):
        if i == n:
            newstr = str.replace(str[n], '')
    return newstr
