#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_int = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                num_int += 1
        except (ValueError, TypeError):
            continue
    print()
    return num_int
