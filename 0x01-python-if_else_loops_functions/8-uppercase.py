#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print("{:c}".format(ord(str[i]) - 32 if ord(str[i]) >= 97 and ord(str[i]) <= 122 else ord(str[i])), end= '')
    print()
