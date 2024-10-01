#!/usr/bin/python3

"""Class Square that defines a square and raises exception when wrong data"""


class Square:
    """Initializes the class with a private instance attribute size"""

    def __init__(self, size=0):
        self.__size = size

    """Property for getting the value of size"""
    @property
    def size(self):
        return (self.__size)

    """method for setting property and implementing type/value verification"""
    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value
