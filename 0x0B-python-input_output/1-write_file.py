#!/usr/bin/python3
"""
"write_file" module writes a string "text" into the file
"""


def write_file(filename="", text=""):
    """Function writes a text into a file"""
    with open(filename, "w", encoding="UTF-8") as f:
        count = f.write(text)
    return count
