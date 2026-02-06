#!/usr/bin/python3
"""
12. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers
    representing the Pascal's triangle of n.
    """
    pascal = []

    if n < 1:
        return pascal

    for i in range(n):
        tmp = []
        if i == 0:
            pascal.append([1])
            continue
        for j in range(i+1):
            if j == 0:
                tmp.append(1)
                continue
            if j == i:
                tmp.append(1)
                continue
            tmp.append(pascal[i-1][j] + pascal[i-1][j-1])
        pascal.append(tmp)
    return pascal
