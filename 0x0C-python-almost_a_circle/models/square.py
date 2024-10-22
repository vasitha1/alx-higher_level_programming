#!/usr/bin/python3
"""
Square module which inherits from rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """This method innitialises the square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Method used to get size out of class"""
        return self.width

    @size.setter
    def size(self, value):
        """Method used to set sieze to height and width"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle"""
        return {"id": self.id,
                "width": self.size,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        """This method creates the string representation of the object"""
        return ("[Square] ({0}) {1}/{2} - {3}".format(self.id, self.x,
                                                      self.y, self.size))
