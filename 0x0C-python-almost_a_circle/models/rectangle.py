#!/usr/bin/python3
"""Implements a rectangle class"""

from models.base import Base
import turtle

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
        ide, x = self.id, self.__x
        y, width, height = self.__y, self.__width, self.__height
        return f"[Rectangle] ({ide}) {x}/{y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """updating with both args and kwargs"""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dict of self"""
        ret_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return ret_dict

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_data)
        instances = [cls.create(**dict_obj) for dict_obj in list_dicts]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as file:
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    file.write("{},{},{},{},{}\n".format(obj.id, obj.width, obj.height, obj.x, obj.y))
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    file.write("{},{},{},{}\n".format(obj.id, obj.size, obj.x, obj.y))

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return []

        instances = []
        for line in lines:
            data = line.strip().split(',')
            if cls.__name__ == "Rectangle":
                instance = cls(int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4]))
            elif cls.__name__ == "Square":
                instance = cls(int(data[0]), int(data[1]), int(data[2]), int(data[3]))
            instances.append(instance)

        return instances
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws all the Rectangles and Squares"""
        turtle.speed(0)  # Set the drawing speed to fastest
        turtle.penup()   # Lift the pen to avoid drawing lines between shapes

        for rectangle in list_rectangles:
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)
            turtle.penup()

        for square in list_squares:
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.penup()

        turtle.done()  # Keep the window open after drawing
