#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    import requests
    import sys

    val = ""
    if len(sys.argv) > 1:
        val = sys.argv[1]

    d = requests.post('http://0.0.0.0:5000/search_user', data={'q': val})
    try:
        res = d.json()
        if res == {}:
            print('No result')
        else:
            print('[{}] {}'.format(res.get('id'), res.get('name')))
    except ValueError:
        print("Not a valid JSON")
