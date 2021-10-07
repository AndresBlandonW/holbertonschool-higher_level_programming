#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    print text with two lines afther each
    specific characters

    Return - a text
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    characters = ['.', '?', ':']
    ck = 0
    for char in text:
        if ck == 0:
            if char == ' ':
                continue
            else:
                ck = 1

        if ck == 1:
            if char in characters:
                print(char)
                print()
                ck = 0
            else:
                print(char, end="")
