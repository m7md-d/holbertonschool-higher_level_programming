#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new = []
    for i in range(len(my_list)):
        if i == idx:
            continue
        new.append(my_list[i])
    my_list[:] = new
    return new
