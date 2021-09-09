#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lon = len(sys.argv)
    if lon == 2:
        print("{} argument:".format(lon-1))
    elif lon == 1:
        print("{} arguments:".format(lon-1))
    else:
        print("{} arguments.".format(lon - 1))
    for i in range(1, lon):
        print("{}:".format(i), str(sys.argv[i]))
