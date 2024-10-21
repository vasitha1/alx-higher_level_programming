#!/usr/bin/python3
"""
The "Base class" module
"""


import json
import os

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

    def to_json_string(list_dictionaries):
        """Displays the JSON representation of a list"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """adding the static method that returns the JSON string"""
        filename = cls.__name__ + ".json"
        json_string = to_json_string(list_objs)
        with open(filename, "w") as f:
            f.write(json_string)

    def from_json_string(json_string):
        """Method that returns the list representation of a json list"""
        if json_string == None or json_string == []:
            return "[]"
        return json.loads(json_string)

    def create(cls, **dictionary):
        """Method that creates  instance with all attributes already set:"""
        dummy = cls(1)
        dummy.update(**dictionary)

        return dummy
        
    def load_from_file(cls):
        """Method returns a list of instances from json file"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return "[]"
        with open(filename, 'r') as f:
            json_string = f.read()

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]
        
