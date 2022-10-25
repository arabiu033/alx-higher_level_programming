#!/usr/bin/python3
""" Imported BaseGeometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A subclass of BaseGeometry """

    def __init__(self, width, height):
        """ Initialize """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
