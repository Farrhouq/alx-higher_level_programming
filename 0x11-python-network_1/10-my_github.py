#!/usr/bin/python3
"""This endpoint gets my id"""

if __name__ == "__main__":
    import requests
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    headers = {"Authorization": f"Bearer {password}",
               'X-GitHub-Api-Version': '2022-11-28',
               'Accept': 'application/vnd.github+json'}
    res = requests.get("https://api.github.com/user", headers=headers)
    print(res.json().get('id'))
