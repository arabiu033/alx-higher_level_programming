#!/usr/bin/python3
""" No Modules Imported """


class Square:
    """ Anothe Square class with mode advance verification """
    __size = 0

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
