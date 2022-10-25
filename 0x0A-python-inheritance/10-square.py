#!/usr/bin/python3
""" Rectange module imorted """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Type class of a square inherit a rectangle"""

    def __init__(self, size):
        """ Initializer """
        super().__init__(size, size)
        self.__size = size
