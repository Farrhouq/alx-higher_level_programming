#!/usr/bin/python3
"""Implements a Square class"""

from .rectangle import Rectangle


class Square(Rectangle):
    """A Square(Rectangle)"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, width):
        self.validate_dimension(width, "width")
        self.width = width
        self.height = width
