#!/bin/usr/python3

"""
    This is the 0-say_my_name module which writes parsed names to the output
"""


def say_my_name(first_name, last_name=""):
    """This is the say_my_name module"""

    if first_name == None or not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
        
    if not isinstance(last_name, str) or last_name == None:
        raise TypeError("last_name must be a string")

    print("My name is {0} {1}".format(first_name, last_name))

