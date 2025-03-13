#!/usr/bin/python3
"""
Module containing the append_write function.
"""

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
