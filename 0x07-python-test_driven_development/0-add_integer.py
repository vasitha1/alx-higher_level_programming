#!/usr/bin/python3

"""
    This is "0-add_integer" module which supplies, add_integer(a, b)
"""


def add_integer(a, b=98):
    """Function that adds two ints"""

    # Handling no input for a
    if a is None:
        raise TypeError("a must be an int")

    threshold = 1e10

    # convert float to int
    if isinstance(a, float):
        if abs(a) > threshold:
            raise ValueError("precision may be lost, a is large Float")

        a = int(a)

    if isinstance(b, float):
        if abs(b) > threshold:
            raise ValueError("precision may be lost, b is a large Float")
        b = int(b)

    # handling non int arguments:
    if not isinstance(a, int):
        raise TypeError("a must be an integer")

    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
