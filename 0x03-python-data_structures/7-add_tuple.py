#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = []
    b = []
    z = []
    for i in range(2):
        if i < len(tuple_a):
            a.append(tuple_a[i])
        else:
            a.append(0)

    for i in range(2):
        if i < len(tuple_b):
            b.append(tuple_b[i])
        else:
            b.append(0)

    for i in range(2):
        z.append(a[i] + b[i])
    return tuple(z)
