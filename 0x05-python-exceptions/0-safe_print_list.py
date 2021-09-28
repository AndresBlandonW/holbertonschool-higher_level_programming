#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num_elem = 0
        for i in range(x):
            print(my_list[i], end="")
            num_elem += 1
        print()
        return num_elem
    except IndexError:
        print()
        return num_elem
