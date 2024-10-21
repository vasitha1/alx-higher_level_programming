#!/usr/bin/python3
"""
This is the module for the "Rectangle" class
"""
from models.base import Base


class Rectangle(Base):
    """Class which defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method innitialises the Rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width"""
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Method to retreive the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method for setting height"""
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")

        if Height <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Method to retreive the value of x"""
        return self.__x

    @height.setter
    def x(self, value):
        """Method for setting x"""
        if not isinstance(x, (int, float)):
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Method to retreive the value of y"""
        return self.__x

    @height.setter
    def y(self, value):
        """Method for setting y"""
        if not isinstance(y, (int, float)):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method to get area"""
        return (self.__height * self.__width)

    def display(self):
        """Method that prints a rectangle with "#" blocks"""
        for i in range(self.__height):
            print()
        for h in range(self.height):
            print(" " * self.x + "#" * self._width)

    def update(self, *args, **kwargs):
        """Method that reassigns attributes with variable number of args"""
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

        else:
            if id:
                self.id = id
            if width:
                self.width = width
            if height:
                self.height = height
            if x:
                self.x = x
            if y:
                self.y = y

    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle"""
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        """Method to print the method as a string literal"""
        return ("[Rectangle] ({0}) {1}/{2} - {3}/{4}".format(self.__id,
                                                             self.__x,
                                                             self.__y,
                                                             self.__width,
                                                             self.__height))
