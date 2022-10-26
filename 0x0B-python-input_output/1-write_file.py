#!/usr/bin/python3
""" No Module imported """


def write_file(filename="", text=""):
    """ Write to a file a text """
    with open(filename, mode="w", encoding="utf-8") as fil:
        return fil.write(text)
