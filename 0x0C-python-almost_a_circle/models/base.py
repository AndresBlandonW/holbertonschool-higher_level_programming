#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """"""
    __nb_objects = 0

    def __init__(self, id=None):
        """"""
        if id is not None:
            self.id = int(id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        of list_objs to a file
        """
        str_rep = ""
        new_list = []
        filename = "{}.json".format(cls.__name__)

        with open(filename, "w") as f:
            if list_objs is None and type(list_objs) is not list:
                f.write("[]")
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())

                str_rep = cls.to_json_string(new_list)
                f.write(str_rep)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string
        representation json_string
        """
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)
