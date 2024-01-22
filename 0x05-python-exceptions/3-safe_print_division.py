#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = int(a) / int(b)
    except ZeroDivisionError:
        return result
    finally:
        print("{}". format(result))
    return result
