#!/usr/bin/env python3
def uppercase(str):

    leng = len(str)
    for i in range(0, leng):
        uppc = ord(str[i])
        if uppc >= 97 and uppc <= 122:
                uppc = uppc - 32
                print(chr(uppc), end="")
        else:
            print(str[i], end="")
