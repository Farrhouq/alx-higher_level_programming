#!/bin/bash
# This script shows the status code
curl -s -w "%{http_code}" $1
