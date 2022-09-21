#!/usr/bin/python3
n = 0;
for i in range(9):
    for j in range(1, 10):
        if i >= j:
            continue
        elif i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=', ')
