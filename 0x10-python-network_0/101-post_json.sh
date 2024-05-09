#!/bin/bash
# This curls a json file
curl -s -H "Content-Type: application/json" -F $2 $1
