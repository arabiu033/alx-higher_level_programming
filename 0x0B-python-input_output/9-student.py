#!/usr/bin/python3
""" No Module Imported """


class Student:
    """ Class to represent a student """

    def __init__(self, fname, lname, age):
        """ Intialize """
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """
        return self.__dict__
