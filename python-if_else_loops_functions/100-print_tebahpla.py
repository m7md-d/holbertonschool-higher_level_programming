#!/usr/bin/python3
up = False
for i in range(26,0,-1):
    if up:
        print("{}".format(chr(i + 64)), end="")
    else:
        print("{}".format(chr(i + 96)), end="")
    up = not up
