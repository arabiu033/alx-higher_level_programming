#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import requests
    import sys

    d = requests.get(sys.argv[1])
    if d.status_code >= 400:
        print("Error code: {}".format(d.status_code))
    else:
        print(d.text)
