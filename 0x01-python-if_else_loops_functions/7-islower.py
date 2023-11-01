#!/usr/bin/python3
def islower(c):
    lower_a = ord('a')
    lower_z = ord('z')

    character_code = ord(c)
    is_lower = lower_a <= character_code <= lower_z

    return is_lower
