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
