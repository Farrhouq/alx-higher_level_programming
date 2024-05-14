#!/usr/bin/python3
"""This queries a search api"""

if __name__ == "__main__":
    import requests
    import sys
    letter = sys.argv[1]
    res = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})
    try:
        if res.json():
            print(f"[{res.json()['id']}] {res.json()['name']}")
        else:
            print("No result")
    except:
        print("Not a valid JSON")
