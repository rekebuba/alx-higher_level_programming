#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ex:
        sys.stderr.write("Exception: {}\n".format(str(ex)))
        return False
    else:
        return True
