#!/usr/bin/python3
def multiple_returns(sentence):
    ltup = []
    ltup = list(sentence)

    if len(sentence) == 0:
        first = "none"
    else:
        first = ltup[0]
    ntup = (len(ltup), first)
    return tuple(ntup)
