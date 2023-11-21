#!/usr/bin/python3
import sys


def safe_function(funct, *args):
    fin = None
    try:
        fin = funct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
    return fin
