#!/usr/bin/python3
""" No module exported """


def print_square(size):
    """ This function print a square of rectangle """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
    
