#!/bin/bash
# This curls a json file
curl -s -H "Content-Type: application/json" -d @$2 $1
