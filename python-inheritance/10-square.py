#!/usr/bin/python3
"""
Module containing Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Instantiation with size.
        size must be private. No getter or setter.
        size must be a positive integer, validated by integer_validator
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        the area() method must be implemented
        """
        return self.__size * self.__size
