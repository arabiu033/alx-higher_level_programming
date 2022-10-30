#!/usr/bin/python3
""" json module imported """
import json


class Base:
    """
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor to initialize instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        objs = []
        for i in range(len(list_objs)):
            objs.append(list_objs[i].to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as fil:
            fil.write(cls.to_json_string(objs))
