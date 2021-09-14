#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rv_my_list = []
    for i in range(len(my_list), 0, -1):
        rv_my_list.append(i)
    print(rv_my_list)
