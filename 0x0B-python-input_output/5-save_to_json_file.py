#!/usr/bin/python3
""" json module imported """
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file,
    using a JSON representation: """
    with open(filename, mode="w", encoding="utf-8") as fil:
        json.dump(my_obj, fil)
