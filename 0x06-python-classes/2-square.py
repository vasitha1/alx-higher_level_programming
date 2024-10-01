#!/usr/bin/python3

"""Class Square that defines a square and raises exception when wrong data"""


class Square:
    """Initializes the class with a private instance attribute size"""

    __size = None

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
