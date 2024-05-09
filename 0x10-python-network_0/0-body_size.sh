#!/bin/bash
# This script takes a url and displays the size of response
curl -s -w "%{size_download}\n" $1 -o /dev/null
