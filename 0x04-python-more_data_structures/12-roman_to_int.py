#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return o
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list = 0
    for j in range(len(roman_string)):
        if j > 0 and roman_dic[roman_string[j]] > roman_dic[roman_string[j - 1]]:
            list += roman_dic[roman_string[j]] - 2 * roman_dic[roman_string[j - 1]]
        else:
            list += roman_dic[roman_string[j]]
    return list
