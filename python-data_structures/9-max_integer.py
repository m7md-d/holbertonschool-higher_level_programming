#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    max = 0
    if ln == 0:
        return None
    for i in my_list:
        if i > max:
            max = i
    return max
