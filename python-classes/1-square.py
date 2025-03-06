#!/usr/bin/python3
"""Module defining a class Square."""

class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
