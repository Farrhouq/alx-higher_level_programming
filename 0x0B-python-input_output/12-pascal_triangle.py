#!/usr/bin/python3
"""Contains a function that returns a list of lists of integers
representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """function that returns a list of lists of integers
representing the Pascal's triangle of n"""
    if n <= 0:
        return []
    prev = [1]
    final = [prev]
    while len(prev) < n:
        inter = [0] + [k for k in prev] + [0]
        prev = [0 for n in range(1, len(prev)+2)]
        for i in range(len(inter)-1):
            prev[i] = inter[i] + inter[i+1]
        final.append(prev)
    return final
