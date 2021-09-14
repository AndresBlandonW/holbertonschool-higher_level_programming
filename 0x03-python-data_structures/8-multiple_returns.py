#!/usr/bin/python3
def multiple_returns(sentence):
    ltup = []
    ltup = list(sentence)
    ntup = (len(ltup), ltup[0])
    return tuple(ntup)
