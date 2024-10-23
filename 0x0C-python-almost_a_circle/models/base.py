#!/usr/bin/python3
"""
The "Base class" module
"""


import json
import os
import csv


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This function innitialises the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Displays the JSON representation of a list"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """adding the static method that returns the JSON string"""
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]\
            if list_objs else []
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list representation of a json list"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method that creates  instance with all attributes already set:"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Method returns a list of instances from json file"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            json_string = f.read()

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves data in CSV format into a file"""

        from models.rectangle import Rectangle
        from models.square import Square

        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as f:
            write = csv.writer(f)
            for item in list_objs:
                if isinstance(item, Rectangle):
                    write.writerow(["Rectangle", item.id, item.width,
                                    item.height, item.x, item.y])
                elif isinstance(item, Square):
                    write.writerow(["Square", item.id, item.size, item.x,
                                    item.y])

    @classmethod
    def load_from_file_csv(cls):
        """Transforms CSV file into a list of object instances"""

        from models.rectangle import Rectangle
        from models.square import Square

        filename = cls.__name__ + ".csv"
        instance = []
        if not os.path.exists(filename):
            return instance
        else:
            with open(filename, "r", newline='') as f:
                read = csv.reader(f)
                for row in read:
                    if row[0] == "Rectangle":
                        instance.append(Rectangle(
                            id=int(row[1]),
                            width=int(row[2]),
                            height=int(row[3]),
                            x=int(row[4]),
                            y=int(row[5])
                        ))
                    elif row[0] == "Square":
                        instance.append(Square(
                            id=int(row[1]),
                            size=int(row[2]),
                            x=int(row[3]),
                            y=int(row[4])
                        ))
        return instance
