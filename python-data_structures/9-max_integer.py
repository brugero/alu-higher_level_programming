#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    if not my_list:
        return None

    biggest = my_list[0]  # Initialize biggest with the first element
    for num in my_list:
        if num > biggest:
            biggest = num

    return biggest
