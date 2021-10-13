#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the s triangle of n
    """
    listp = []

    if n <= 0:
        return listp

    for i in range(1, n + 1):
        num = 1
        listp2 = []

        for j in range(1, i + 1):
            num = int(num * (i - j) / j)
            if listp2 == []:
                listp2.append(1)
            if j < i:
                listp2.append(num)
        listp.append(listp2)
    return listp
