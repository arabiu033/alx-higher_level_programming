#!/usr/bin/python3
""" No Modules Imported """


class Square:
    """ Anothe Square class with mode advance verification """
    __size = 0

    def __init__(self, size=0):
        """ Initial the class variables """
        self.size = size

    @property
    def size(self):
        """ Serve as a getter to return back the class size """
        return self.__size

    @size.setter
    def size(self, size=0):
        """ Set the size of the square to a new value """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return the area of the square """
        return self.size * self.size

    def __eq__(self, other):
        """ Check the equality of two instances """
        return self.size == other.size

    def __lt__(self, other):
        """ Check less than between two instances """
        return self.size < other.size

    def __gt__(self, other):
        """ Check greaer than between two instances """
        return self.size > other.size

    def __le__(self, other):
        """ Check less than or equal to between two instances """
        return self.size <= other.size

    def __ge__(self, other):
        """ Check greater than or equal to between two instances """
        return self.size >= other.size

    def __ne__(self, other):
        """ Check not equal to between two instances """
        return self.size != other.size
