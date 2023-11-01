#!/usr/bin/python3
def uppercase(str):
    for i in str:
        lower_a = ord('a')
        lower_z = ord('z')
        if lower_a <= ord(i) <= lower_z:
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print()
