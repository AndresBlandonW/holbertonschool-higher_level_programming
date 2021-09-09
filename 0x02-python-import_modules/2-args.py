#!/usr/bin/python3
import sys
lon = len(sys.argv)
if lon != 0:
    print("{} arguments:".format(lon-1))
    for i in range(1, lon):
        print("{}:".format(i), str(sys.argv[i]))
else:
    print("0 arguments.")
