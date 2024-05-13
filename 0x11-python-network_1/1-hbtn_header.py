#!/usr/bin/python3
"""This checks a header value"""

if __name__ == "__main__":
    import urllib.request
    import sys
    

    
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.get_header('X-Request-Id'))