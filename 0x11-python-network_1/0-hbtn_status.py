#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        d = res.read()
        print('Body response:')
        print('\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'.format(
            type(d), d, d.decode('utf-8')))
