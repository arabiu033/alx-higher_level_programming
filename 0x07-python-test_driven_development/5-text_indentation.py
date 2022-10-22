#!/usr/bin/python3
""" No mudule imported """


def text_indentation(text=0):
    """ prints a text with 2 new lines after each of these characters: ., ? and : """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = ".\n\n".join(text.split(". "))
    text = "?\n\n".join(text.split("? "))
    text = ":\n\n".join(text.split(": "))
    print(text, end="")
