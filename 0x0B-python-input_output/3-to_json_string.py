#!/usr/bin/python3
"""
to_json_string module returns the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """Function decodes string to jSON"""
    return json.dumps(my_obj)
