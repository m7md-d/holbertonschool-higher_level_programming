#!/usr/bin/python3
def uppercase(str):
    str1 = list(str)
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            str1[i] = chr(ord(str1[i]) - 32)
    print("{}".format("".join(str1)))
