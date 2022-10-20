#!/usr/bin/python3
""" No module imported """


def add_integer(a, b=98):
    """ This function return the addition of two numbers """
    if (type(a) != int and type(a) != float) or \
       a is float('inf') or a is float('-inf') or a != a:
        raise TypeError("a must be an integer")

    if (type(b) != int and type(b) != float) or \
       b is float('inf') or b is float('-inf') or b != b:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
