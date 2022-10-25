#!/usr/bin/python3
""" No module imported """

class MyInt(int):
    """Type class of MyInt inherit int type"""

    def __eq__(self, other):
        """ Opposite of parent method """
        return self.real != other

    def __ne__(self, other):
        """ Opposit of parent method """
        return self.real == other
