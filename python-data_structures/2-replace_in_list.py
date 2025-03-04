#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list[:]  # Create a copy of the list
        new_list[idx] = element
        return new_list
