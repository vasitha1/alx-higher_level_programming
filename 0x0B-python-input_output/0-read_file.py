#!/usr/bin/python3
"""
This module 'read_file' opens a file and reads it
"""


def read_file(filename=""):
    """Function that reads the file and prints it's content"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
