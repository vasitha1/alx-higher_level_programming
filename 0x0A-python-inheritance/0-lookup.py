#!/usr/bin/python3

"""
The lookup function that returns the list of available attributes and methods
"""


def lookup(obj):
    return [dir(obj)]
