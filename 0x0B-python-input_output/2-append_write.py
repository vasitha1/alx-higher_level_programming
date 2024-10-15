#!/usr/bin/python3
"""
 function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Appends the "text" to filename"""
    with open(filename, "a", encoding="UTF-8") as f:
        count = f.write(text)
    return (count)
