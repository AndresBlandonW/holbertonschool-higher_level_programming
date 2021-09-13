#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    lon = len(sys.argv)

    if (lon != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    num1 = int(sys.argv[0])
    num2 = int(sys.argv[2])
    ope = str(sys.argv[1])

    if ope == "+":
        print("{} {} {} = {}".format(num1, num2, ope, add(num1, num2)))
    elif ope == "-":
        print("{} {} {} = {}".format(num1, num2, ope, sub(num1, num2)))
    elif ope == "/":
        print("{} {} {} = {}".format(num1, num2, ope, div(num1, num2)))
    elif ope == "*":
        print("{} {} {} = {}".format(num1, num2, ope, mul(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
