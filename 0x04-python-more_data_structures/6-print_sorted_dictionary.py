#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    slist = dict(sorted(a_dictionary.items(), key=lambda x: x[0]))

    for key, val in slist.items():
        print("{}: {}".format(key, val))
