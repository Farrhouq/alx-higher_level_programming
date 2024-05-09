#!/bin/bash
curl -s -L -w "%{http_code}" -o response.txt $1 | grep -q 200 && cat response.txt
