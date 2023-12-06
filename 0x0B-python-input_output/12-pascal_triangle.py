#!/usr/bin/python3
"""Creating a function that returns integers of Pascal"""


def pascal_triangle(n):
    """
    n: integer value
    Return: an empty list if n <= 0
    """
    if n <= 0:
        return []

    pascal = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        pascal.append(row)

    return pascal
