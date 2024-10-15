#!/usr/bin/python3

"""
"MyList" module is used to demostrate class inheritance
"""


class MyList(list)
    """Class which inherits from list"""

    def print_sorted(self):
        """Method that prints list in sorted order"""
        print(sorted(self))
