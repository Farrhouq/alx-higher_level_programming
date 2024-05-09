#!/bin/bash
curl -Ls -w "%{http_code}" -o /dev/null $1 | grep -q 200 && cat response.txt
