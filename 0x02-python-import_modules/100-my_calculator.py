#!/usr/bin/python3.8
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if ord(argv[2]) < 42 or ord(argv[2]) > 47 or ord(argv[2]) == 46:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if ord(argv[2]) == 42:
        print("{} * {} = {}".format(argv[1], argv[3],
                                    mul(int(argv[1]), int(argv[3]))))
    if ord(argv[2]) == 43:
        print("{} + {} = {}".format(argv[1], argv[3],
                                    add(int(argv[1]), int(argv[3]))))
    if ord(argv[2]) == 45:
        print("{} - {} = {}".format(argv[1], argv[3],
                                    sub(int(argv[1]), int(argv[3]))))
    if ord(argv[2]) == 47:
        print("{} / {} = {}".format(argv[1], argv[3],
                                    div(int(argv[1]), int(argv[3]))))
