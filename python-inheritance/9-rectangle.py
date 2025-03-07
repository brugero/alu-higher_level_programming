#!/usr/bin/python3
"""
Module containing Rectangle class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height.
        width and height must be private. No getter or setter.
        width and height must be positive integers, validated by integer_validator
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        the area() method must be implemented
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print() should print, and str() should return,
        the following rectangle description: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
