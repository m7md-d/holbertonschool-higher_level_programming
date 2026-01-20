#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for i in my_list:
        if j >= x:
            break
        try:
            print(i, end="")
            j += 1
        except:
            break

    print()
    return j
