#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    ln = len(argv)
    if ln == 1:
        print("0 arguments.")
    elif ln == 2:
        print(f"1 argument:\n1: {argv[1]}")
    else:
        print(f"{ln - 1} arguments:")
        for i in range(1, ln):
            print(f"{i}: {argv[i]}")
