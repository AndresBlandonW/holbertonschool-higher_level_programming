#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    lon = len(sys.argv) - 1

    if (lon != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ope = str(sys.argv[2])

    if ope == "+":
        print("{} {} {} = {}".format(a, ope, b, add(a, b)))
    elif ope == "-":
        print("{} {} {} = {}".format(a, ope, b, sub(a, b)))
    elif ope == "/":
        print("{} {} {} = {}".format(a, ope, b, div(a, b)))
    elif ope == "*":
        print("{} {} {} = {}".format(a, ope, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
