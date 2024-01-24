#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxi = 0
    ret = None
    for key, val in a_dictionary.items():
        if val >= maxi:
            maxi = val
            ret = key
    return ret
