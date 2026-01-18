#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        c = ""
        for j in i:
            print("{}{:d}".format(c, j), end="")
            c = " "
        print()
