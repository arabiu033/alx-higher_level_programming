#!/usr/bin/python3
""" Rectange class imported """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a Square is a special Rectangle, so it makes
    sense this class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the instances of Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if len(args) != 0:
            self.id = args[0]
            if len(args) == 1:
                return
            self.size = args[1]
            if len(args) == 2:
                return
            self.x = args[2]
            if len(args) == 3:
                return
            self.y = args[3]

        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
