#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    num = 0
    big = 1
    r_ln = len(roman_string)

    for i in range(r_ln - 1, -1, -1):
        tmp = roman.get(roman_string[i], 0)
        if tmp >= big:
            num += tmp
            big = tmp
        else:
            num -= tmp
    return num
