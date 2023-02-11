#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import requests
    import sys

    d = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(d.text)
