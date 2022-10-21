#!/usr/bin/python3
""" No module imported """


def matrix_divided(matrix, div):
    """ This function divide a list base on the div given """
    if len(matrix) == 0:
        return []

    if (type(div) != int and type(div) != float) or \
       div is float('inf') or div is float('-inf') or div != div:
        raise TypeError("div must be a number")

    if div == 0 or div == 0.0:
        raise ZeroDivisionError("division by zero")

    if (type(matrix[0]) == list):
        rowsize = len(matrix[0])

    for i in range(len(matrix)):

        if type(matrix[i]) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if rowsize != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

        for b in range(len(matrix[i])):
            a = matrix[i][b]
            if (type(a) != int and type(a) != float) or \
               a is float('inf') or a is float('-inf') or a != a:
                raise TypeError(
                    "matrix must be a matrix (list of lists)" +
                    " of integers/floats")

    inner = []
    outer = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            val = matrix[i][j]
            inner.append(round(val / div, 2))
        outer.append(inner[:])
        inner = []

    return outer
