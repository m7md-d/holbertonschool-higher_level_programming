#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    ln = len(argv)
    if ln > 1:
        for i in range(1, ln):
            total += int(argv[i])
    print(total)
