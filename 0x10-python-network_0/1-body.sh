#!/bin/bash
curl -Ls -w "%{http_code}" -o response.txt $1 | grep -q 200 && cat response.txt
