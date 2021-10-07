#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    check the values of matrix,
    check the div
    
    Return - matrix of all divided elements
    """
    if type(div) is float:
        div = int(div)
    if type(div) is not int:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for i in matrix:
        if type(i) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError('Each row of the matrix must have the same size')

    subl = [[round(item / div, 2) for item in subl] for subl in matrix]
    return subl
