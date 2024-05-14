#!/usr/bin/python3
"""This module displays the error"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
