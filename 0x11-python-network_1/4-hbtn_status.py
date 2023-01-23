#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import requests

    d = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}\n\t- content: {}'.format(
        type(d.text), d.text))
