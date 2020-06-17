#! /usr/bin/env python

import bs4
from bs4 import BeautifulSoup

import requests
import jsbeautifier
import base64



r = requests.get('https://www.hackthebox.eu/js/inviteapi.min.js')
print(r.encoding)
print(r.text)

print(r.headers['content-type'])
print(r.content)

print('Here comes the beautified unpacked json!!!!')
print('\n')

script = r.content
print(jsbeautifier.beautify(script))

print('Automate some more!!! ')


p = requests.post('https://www.hackthebox.eu/api/invite/generate')
print(p.text)

Main_dictionary = eval(p.text)
print(type(Main_dictionary))

for key, value in Main_dictionary.items():
    if key == "data":
        filling = value
        print filling
        print(type(filling))
        for subkey, subvalue in filling.items():
            if subkey == 'code':
                print('This is your invite code: ')
                print(base64.b64decode(subvalue))
