#!/usr/bin/python3
""" Base Module Imported """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor to initialize instances """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Return the width value """
        return self.__width

    @property
    def height(self):
        """ Return the height value """
        return self.__height

    @property
    def x(self):
        """ Return the x value """
        return self.__x

    @property
    def y(self):
        """ Return the y value """
        return self.__y

    @x.setter
    def x(self, x):
        """ Set the value of x """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """ Set the value of y """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @width.setter
    def width(self, width):
        """ Set the value for width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ Set the value for height """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    def area(self):
        """ Return the area of the Rectangle """
        return self.height * self.width

    def display(self):
        """
        prints in stdout the Rectangle
        instance with the character #
        """
        for a in range(self.y):
            print()
        for i in range(self.height):
            for b in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if len(args) != 0:
            self.id = args[0]
            if len(args) == 1:
                return
            self.width = args[1]
            if len(args) == 2:
                return
            self.height = args[2]
            if len(args) == 3:
                return
            self.x = args[3]
            if len(args) == 4:
                return
            self.y = args[4]

        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
