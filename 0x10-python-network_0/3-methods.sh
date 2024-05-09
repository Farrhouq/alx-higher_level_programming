#!/bin/bash
# This script displays the allowed method for url
curl -sI -X OPTIONS $1 | grep  "Allow" | cut -d ':' -f 2-
