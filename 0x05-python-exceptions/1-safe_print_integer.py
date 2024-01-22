#!usr/bin/python3
def safe_print_integer(value):
    try:
        result = int(value)
        print("{:d}".format(result))
    except ValueError:
        return False
    else:
        return True
