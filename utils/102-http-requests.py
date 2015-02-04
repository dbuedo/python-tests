

print "requests is a HTTP library for human beings"

import requests

print "Simple GET request"
print "GET 'https://api.github.com/events'"
response = requests.get('https://api.github.com/events')
print "Response:", response
print "Content:", response.text

print "#"*50

print "Simple POST request"
print "POST 'http://httpbin.org/post'"
response = requests.post("http://httpbin.org/post")
print "Response:", response
print "Content:", response.text

print "#"*50

print "GET request + params"
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get("http://httpbin.org/get", params=payload)
print "Response:", response
print "Content:", response.text


