#!/usr/bin/python3
""" Module Imported """
import math


class MagicClass:
    """ Magic Class is created based on python bytecode """
    def __init__(self, radius=0):
        """ Initialize instances """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Return the area of the circle """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ Return the circumferece """
        return (2 * math.pi * self.__radius)
