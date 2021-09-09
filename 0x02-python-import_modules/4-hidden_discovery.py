#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    modl = dir(hidden_4)
    for i in range(len(modl)):
        if(modl[i][0] != '_'):
            print(modl[i])
