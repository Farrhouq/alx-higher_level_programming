#!/usr/bin/python3
"""Implements a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_dimension(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_non_negative(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_non_negative(value, "y")
        self.__y = value

    def validate_dimension(self, value, attribute):
        """validates a dimension"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))
        if value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def validate_non_negative(self, value, attribute):
        """validates a dimension"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attribute))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))

    def area(self):
        """returns the area"""
        return self.__width * self.__height

    def display(self):
        """prints out the rectangle"""
        for i in range(self.__y):
            print()
        for _ in range(self.height):
            for j in range(self.__x):
                print(' ', end='')
            print("#" * self.width)

    def __str__(self):
        return (f"[Rectangle]({self.id}) {self.__x} /
                {self.__y} - {self.__width}/{self.__height}")

    # def update(self, *args):
    #     arg_count = len(args)
    #     if arg_count >= 1:
    #         self.id = args[0]
    #     if arg_count >= 2:
    #         self.width = args[1]
    #     if arg_count >= 3:
    #         self.height = args[2]
    #     if arg_count >= 4:
    #         self.x = args[3]
    #     if arg_count >= 5:
    #         self.y = args[4]

    def update(self, *args, **kwargs):
        """updating with both args and kwargs"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
