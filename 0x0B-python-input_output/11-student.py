#!/usr/bin/python3
""" No Module Imported """


class Student:
    """ Class to represent a student """

    def __init__(self, fname, lname, age):
        """ Intialize """
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if attrs is not None:
            return dict((a, b) for (a, b) in
                        self.__dict__.items() if a in attrs)
        return self.__dict__

    def reload_from_json(self, json):
        """  replaces all attributes of the Student instance """
        self.__dict__ = dict(json)
