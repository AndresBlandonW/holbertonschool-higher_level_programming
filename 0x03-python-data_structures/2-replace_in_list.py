#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    cop_my_list = my_list.copy()
    if idx >= len(my_list):
        return cop_my_list
    elif idx < 0:
        return cop_my_list
    else:
        cop_my_list[idx] = element
        return cop_my_list
