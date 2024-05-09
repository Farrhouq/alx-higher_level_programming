#!/bin/bash
# This script shows the status code
curl -s -w -o /dev/null "%{http_code}" $1
