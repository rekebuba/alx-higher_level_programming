#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    arguments = argv[1:]
    length = len(arguments)

    if length == 0:
        print("0 arguments.")
    else:
        print(f"{length} argument{'s' if length != 1 else ''}:")
    a = 1
    for arg in arguments:
        print("{}: {}".format(a, arg))
        a = a + 1
