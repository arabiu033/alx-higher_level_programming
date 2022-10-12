#!/usr/bin/python3
""" No Modules Imported """


class Square:
    """ Anothe Square class with mode advance verification """
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """ Initial the class variables """
        self.size = size
        self.position = position

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
        """ Print the square using # with adjusted position """
        if not self.size:
            print()
            return

        for i in range(self.position[1]):
            print()

        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()

    @property
    def position(self):
        """ return the positioon value """
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        """ Set the amount of space needed for the printing """
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        """ Make the class instances to be use anywhere string is used """
        strr = ""
        if not self.size:
            return ""

        for i in range(self.position[1]):
            strr += "\n"

        for i in range(self.size):
            for k in range(self.position[0]):
                strr += " "
            for j in range(self.size):
                strr += "#"
            strr += "\n" if self.size - i > 1 else ""
        return strr
