#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        r = fct(*args)
        return r
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error))
        return None
