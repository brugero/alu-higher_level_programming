#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list."""
    unique_integers = set()
    total_sum = 0
    for num in my_list:
        if isinstance(num, int) and num not in unique_integers:
            total_sum += num
            unique_integers.add(num)
    return total_sum
