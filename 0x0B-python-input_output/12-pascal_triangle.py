#!/usr/bin/python3
""" No Module Imported """


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n: """
    if n <= 0:
        return []

    outer = [[1]]
    for i in range(n):
        inner = []
        print(len(outer[i]))
        for j in range(len(outer[i])):
            if j == 0 or j == len(outer[i]) - 1:
                inner.append(outer[i][j])
                continue
            inner.append(outer[i][j] + outer[i][j + 1])

            return outer
