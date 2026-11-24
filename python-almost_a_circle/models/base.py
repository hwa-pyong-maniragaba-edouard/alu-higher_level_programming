#!/usr/bin/python3
"""Module that defines the Base class."""
import json


class Base:
    """Base class that manages the id attribute for all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): optional id to assign to the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): a list of dictionaries.

        Returns:
            "[]" if list_dictionaries is None or empty, otherwise
            the JSON string of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        The file is named <Class name>.json and is overwritten if it exists.

        Args:
            list_objs (list): a list of instances inheriting from Base.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string (str): a string representing a list of dictionaries.

        Returns:
            An empty list if json_string is None or empty, otherwise
            the list represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary: key/value pairs used as attributes via update.

        Returns:
            A new instance of cls updated with the given values.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json.

        Returns:
            An empty list if the file doesn't exist, otherwise a list
            of instances of cls.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]
