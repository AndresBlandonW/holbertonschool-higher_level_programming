#!/usr/bin/python3
def multiple_returns(sentence):
    ltup = []
    ltup = list(sentence)

    if sentence is None or sentence == "":
        ntup = (0, None)
    else:
        ntup = (len(ltup), ltup[0])
    return tuple(ntup)
