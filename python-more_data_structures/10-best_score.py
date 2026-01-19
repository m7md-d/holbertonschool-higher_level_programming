#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = 0
    best_name = ""
    for i in a_dictionary.keys():
        if a_dictionary[i] > best:
            best = a_dictionary[i]
            best_name = i
    return best_name
