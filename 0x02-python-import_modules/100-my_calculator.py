#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    args = argv[1:]
    if len(args) != 3:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    a = args[0]
    b = args[2]
    sign = args[1]

    if sign not in operators:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    result = operators[sign](int(a), int(b))

    print('{} {} {} = {}'.format(a, sign, b, result))
