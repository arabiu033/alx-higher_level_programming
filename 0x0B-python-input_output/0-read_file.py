#!/usr/bin/python3
""" No Module Imported """


def read_file(filename=""):
    """ Print the content of a file """
    with open(filename, encoding="utf-8") as fil:
        print(fil.read(), end="")
