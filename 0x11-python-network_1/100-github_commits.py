#!/usr/bin/python3
"""This script gets repos"""

if __name__ == "__main__":
    import requests
    import sys
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    res = requests.get(
        f"https://api.github.com/repos/{owner}/{repo_name}/commits",
        headers={
            'X-GitHub-Api-Version': '2022-11-28',
            'Accept': 'application/vnd.github+json'})
    try:
        for commit in sorted(res.json(), key=lambda x: x['commit']['author']['date']):
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    except Exception as e:
        print(e)
