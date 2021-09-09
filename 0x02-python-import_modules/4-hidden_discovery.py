#!/usr/bin/python3
import sys
import hidden_4 as hidden

for i in dir(hidden):
    if i[0:2] != "__":
        print(i)
