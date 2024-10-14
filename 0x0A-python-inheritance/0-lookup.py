#!/usr/bin/python3

"""
The "lookup function" that returns the list of available attributes and methods
"""


def lookup(obj):
    """lookup function looking for availaible attributes in obj"""
    return [dir(obj)]
