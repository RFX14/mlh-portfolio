#!/bin/sh

url="https://miyabi.duckdns.org"

resp=$(curl -s -w "%{http_code}" GET $url)
result=${resp: -3}
if [[ $result == 200 ]]; then
    echo "Test 1: PASS"
    exit 1
else 
    echo "Test 1: FAIL, Result: $result"
    exit 0
fi

