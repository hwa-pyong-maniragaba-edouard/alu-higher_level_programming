#!/usr/bin/python3
"""Base module."""
import json


class Base:
    """Base class that manages id attribute for all other classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize with a given id or an auto-incremented one."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string of a list of objects to <Class name>.json."""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        data = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, "w", encoding="utf-8") as f:
            f.write(data)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = cls.from_json_string(f.read())
        except IOError:
            return []
        return [cls.create(**d) for d in data]
