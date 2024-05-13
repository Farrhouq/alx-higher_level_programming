#!/usr/bin/python3
"""This checks a header value"""

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        res = response.read()
        print("Body response:")
        print(f"\t- type: {type(res)}")
        print(f"\t - content: {res}")
        print(f"\t - utf8 content: {res.decode('utf-8')}")
