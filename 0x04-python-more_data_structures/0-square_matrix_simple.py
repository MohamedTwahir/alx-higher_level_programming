#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """A function that computes square value using map and labda"""
    return list(map(lambda x: list(map(lambda y: y * y, x)), matrix))
