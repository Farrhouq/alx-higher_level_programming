#!/bin/bash
# This script displays the allowed method for url
curl -sI -X OPTIONS  0.0.0.0:5000/route_4 | grep -i Allow | cut -c 8- | sed 's/\r$//'
