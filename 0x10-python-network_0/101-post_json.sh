#!/bin/bash
# This curls a json file
curl -s -H "Content-Type: application/json" -F "file=$2" $1
