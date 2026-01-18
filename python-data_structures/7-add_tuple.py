#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lna = len(tuple_a)
    lnb = len(tuple_b)
    a = 0
    b = 0
    if lna >= 1:
        a += tuple_a[0]
    if lna >= 2:
        b += tuple_a[1]
    if lnb >= 1:
        a += tuple_b[0]
    if lnb >= 2:
        b += tuple_b[1]
    new = (a, b)
    return new
