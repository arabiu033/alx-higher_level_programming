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
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        if type(list_objs) is not list:
            list_objs = []
        filename = cls.__name__ + ".json"
        objs = []
        for i in range(len(list_objs)):
            objs.append(list_objs[i].to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as fil:
            fil.write(cls.to_json_string(objs))

    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        dummy = cls(5, 5, 5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """  that returns a list of instances """
        filename = cls.__name__ + ".json"
        with open(filename, encoding="utf-8") as fil:
            objs = fil.read()

        list_objs = Base.from_json_string(objs)
        list_of_instances = []
        for i in range(len(list_objs)):
            list_of_instances.append(cls.create(**list_objs[i]))
        return list_of_instances
