#!/usr/bin/python3
""" No Module imported """


def inherits_from(obj, a_class):
    """ Return true only if obj inherit from a_class """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
