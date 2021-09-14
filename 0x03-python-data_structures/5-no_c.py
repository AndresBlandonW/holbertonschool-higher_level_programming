#!/usr/bin/python3
def no_c(my_string):
    new_my_string = []
    new_my_string = list(my_string)
    for i in range(len(new_my_string)):
        if new_my_string[i] == "c" or new_my_string[i] == "C":
            new_my_string[i] = ""
    str1 = ""
    for ele in new_my_string:
        str1 += ele
    return str1
