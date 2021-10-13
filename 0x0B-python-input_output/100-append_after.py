#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, "r") as f:
        list = []
        lines = len(f.readlines())
        f.seek(0)

        for i in range(lines):
            line = f.readline()
            list.append(line)
            if search_string in line:
                list.append(new_string)

    with open(filename, "w") as f:
        f.writelines(list)
