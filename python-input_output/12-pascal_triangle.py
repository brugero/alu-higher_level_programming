#!/usr/bin/python3
"""
Module containing the pascal_triangle function.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists of integers representing the Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
