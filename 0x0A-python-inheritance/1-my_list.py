#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """
    Inherits from list
    """
    def print_sorted(self):
        """
        prints the list sorted
        """
        alist = self[:]
        alist.sort()
        print(alist)
