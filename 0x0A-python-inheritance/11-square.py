#!/usr/bin/python3
""" Rectange module imported """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Type class of a square inherit a rectangle"""

    def __init__(self, size):
        """ Initializer """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Work as string """
        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string
