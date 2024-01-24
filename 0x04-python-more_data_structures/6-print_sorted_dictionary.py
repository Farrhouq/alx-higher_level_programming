#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys = list(a_dictionary.keys()).sort()
    for key in dict_keys:
        print(key, ": ", a_dictionary[key])
