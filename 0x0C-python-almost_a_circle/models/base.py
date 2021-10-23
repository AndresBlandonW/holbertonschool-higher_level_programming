#!/usr/bin/python3
"""Base Class"""
import json
import csv


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init method for Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attrib already set"""
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        new_list = []
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as f:
                    dic = cls.from_json_string(f.read())

                    for i in dic:
                        obj = cls.create(**i)
                        new_list.append(obj)
                    return new_list
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in csv"""
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, mode="w", encoding="utf-8", newline="") as csv_f:
            csv_obj = csv.writer(csv_f)
            if cls.__name__ == "Rectangle":
                [csv_obj.writerow([obj.id, obj.width, obj.height,
                                  obj.x, obj.y]) for obj in list_objs]
            elif cls.__name__ == "Square":
                [csv_obj.writerow([obj.id, obj.size,
                                  obj.x, obj.y]) for obj in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """ that serializes and deserializes in CSV"""
        file_name = "{}.csv".format(cls.__name__)
        try:
            with open(file_name, mode="r", encoding="utf-8", newline="")\
                    as csv_f:
                csv_obj = csv.reader(csv_f)
                if cls.__name__ == "Rectangle":
                    destiny = ['id', 'width', 'height', 'x', 'y']
                    return [(cls.create(**{destiny[index]: int(el) for index,
                                        el in enumerate(row)}))
                            for row in csv_obj]
                elif cls.__name__ == "Square":
                    destiny = ['id', 'size', 'x', 'y']
                    return [(cls.create(**{destiny[index]: int(el) for index,
                                        el in enumerate(row)}))
                            for row in csv_obj]
        except IOError:
            return []
