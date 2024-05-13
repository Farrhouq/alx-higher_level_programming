#!/usr/bin/python3
"""This module checks your status"""

import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    res = response.read()
    print("Body response:")
    print(f"\t- type: {type(res)}")
    print(f"\t - content: {res}")
    print(f"\t - utf8 content: {res.decode('utf-8')}")
