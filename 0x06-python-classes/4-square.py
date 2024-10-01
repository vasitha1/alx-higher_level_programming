#!/usr/bin/python3

"""Class Square that defines a square and raises exception when wrong data"""


class Square:
    """Initializes the class with a private instance attribute size"""

    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        """Gets the size of square"""
        return self.__size

    @size.setter
    def size(self, value=0):
        """sets the size of square ensuring that it is a non-negative int"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    """Area method to find area of square"""
    def area(self):
        return self.__size ** 2
