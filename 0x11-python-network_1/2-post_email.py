#!/usr/bin/python3
"""This module sends a post request"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    data = urllib.parse.urlencode(data)
    data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read())
