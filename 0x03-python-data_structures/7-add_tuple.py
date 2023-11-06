#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length_a = len(tuple_a)
    length_b = len(tuple_b)
    if length_a >= 1:
        v_a = tuple_a[0]
    else:
        v_a = 0

    if length_b >= 1:
        v_b = tuple_b[0]
    else:
        v_b = 0

    if length_a >= 2:
        v_a = tuple_a[1]
    else:
        v_a = 0

    if length_b >= 2:
        v_b = tuple_b[1]
    else:
        v_b = 0

    new_tuple = (v_a + v_b, v_a + v_b)
    return new_tuple
