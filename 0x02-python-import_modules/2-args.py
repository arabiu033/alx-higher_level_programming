#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{}".format(len(argv) - 1), end=' argument' if len(argv) == 2
          else ' arguments')
    print("", end='.\n' if len(argv) == 1 else ':\n')
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
