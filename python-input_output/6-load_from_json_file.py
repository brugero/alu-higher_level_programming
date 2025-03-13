#!/usr/bin/python3
"""
Module containing the load_from_json_file function.
"""
import json

def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
