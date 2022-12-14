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

    def my_print(self):
        """ Print the area of the square in stdout using # """
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
        if not self.size:
            print()
