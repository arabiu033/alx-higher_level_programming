#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import requests
    import sys

    d = requests.get(sys.argv[1])
    print(d.headers.get('X-Request-Id'))
