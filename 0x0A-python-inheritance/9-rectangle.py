#!/usr/bin/python3
"""Contains a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Implements a Rectangle class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """implements the area"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"
