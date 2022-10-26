#!/usr/bin/python3
""" No Module imported """


def append_write(filename="", text=""):
    """ Append to a file a text """
    with open(filename, mode="a", encoding="utf-8") as fil:
        return fil.write(text)
