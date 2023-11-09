#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for j in my_list:
        if j == search:
            new.append(replace)
        else:
            new.append(j)
    return new
