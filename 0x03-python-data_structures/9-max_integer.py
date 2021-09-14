#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or my_list == "":
        return None
    maxi = 0
    for i in range(len(my_list)):
        if int(my_list[i]) > maxi:
            maxi = int(my_list[i])
    return maxi
