#!/bin/sh

register_url="https://miyabi.duckdns.org/register"
login_url="https://miyabi.duckdns.org/login"

#Register: Username is req
resp=$(curl -s -w "%{http_code}" -X POST -d "username=" $register_url)
result=${resp: -3}
if [[ $result == 418 ]]; then
	echo "Test 1: PASS"
else 
	echo "Test 1: FAIL, Result: $result"
fi

#Register: Password is req
resp=$(curl -s -w "%{http_code}" -X POST -d "username=coffee&password=" $register_url)
result=${resp: -3}
if [[ $result == 418 ]]; then
    echo "Test 2: PASS"
else
    echo "Test 2: FAIL, Result: $result"
fi

#Register: Username exists
resp=$(curl -s -w "%{http_code}" -X POST -d "username=coffeemate&password=123" $register_url)
result=${resp: -3}
if [[ $result == 418 ]]; then
    echo "Test 3: PASS"
else
    echo "Test 3: FAIL, Result: $result"
fi

#Register: Success
resp=$(curl -s -w "%{http_code}" -X POST -d "username=coffees&password=123" $register_url)
result=${resp: -3}
if [[ $result == 200 ]]; then
    echo "Test 4: PASS"
else
    echo "Test 4: FAIL, Result: $result"
fi

#Login: Incorrect username
resp=$(curl -s -w "%{http_code}" -X POST -d "username=" $login_url)
result=${resp: -3}
if [[ $result == 418 ]]; then
    echo "Test 5: PASS"
else
    echo "Test 5: FAIL, Result: $result"
fi

#Login: Incorrect password
resp=$(curl -s -w "%{http_code}" -X POST -d "username=coffees&password=1234" $login_url)
result=${resp: -3}
if [[ $result == 418 ]]; then
    echo "Test 6: PASS"
else
    echo "Test 6: FAIL, Result: $result"
fi

#Login: Success
resp=$(curl -s -w "%{http_code}" -X POST -d "username=coffees&password=123" $login_url)
result=${resp: -3}
if [[ $result == 200 ]]; then
    echo "Test 7: PASS"
else
    echo "Test 7: FAIL, Result: $result"
fi
