#!/usr/bin/python3
""" No module imported """


class LockedClass:
    """ Locked class to prevent creation of new instances """
    __slots__ = ['first_name']
    pass
