#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    for j in my_list:
        if j not in new:
            new.append(j)
    return sum(new)
