#!/usr/bin/python3
"""Contains a Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implements a Rectangle class"""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates the area of the square"""
        return self.__size ** 2

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
