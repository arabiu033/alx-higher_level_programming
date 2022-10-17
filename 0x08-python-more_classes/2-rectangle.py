#!/usr/bin/python3
""" No Module Imported """


class Rectangle:
    """ A rectangle class with some attribures declared

    setter and getters methods include """
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """ Intialize the class instances """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Return the value of width """
        return self.__width

    @property
    def height(self):
        """ Return the value of height """
        return self.__height

    @width.setter
    def width(self, width):
        """ Set the width to a new value """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ Set the height to a new value """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ Return the area value of the rectangle """
        return self.height * self.width

    def perimeter(self):
        """ Return the perimater of the rectangle """
        return 2*self.height + 2*self.width
