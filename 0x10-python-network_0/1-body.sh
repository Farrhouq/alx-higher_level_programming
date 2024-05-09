#!/bin/bash
# This script writes the body of a 200
curl -s -L -w "%{http_code}" -o response.txt $1 | grep -q 200 && cat response.txt
