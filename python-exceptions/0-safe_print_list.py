#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    new = []
    for i in my_list:
        if j >= x:
            break
        new.append(i)
        j += 1
    print(new)
    return j
