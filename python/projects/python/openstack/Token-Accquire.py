#!/usr/bin/python
import httplib
import json
url = "9.123.137.200:5000"
osuser = "admin"
ospassword = "Passw0rd"
params = '{"auth":{"passwordCredentials":{"username":"admin","password":"Passw0rd"},"tenantId":"fd881b9cdc904e33871d5038f6397c4c"}}'
headers = {"Content-Type":"application/json"}
conn = httplib.HTTPConnection(url)
conn.request("POST","/v2.0/tokens",params,headers)

response = conn.getresponse()
data  = response.read()
dd = json.loads(data)

conn.close()
print type(dd)
apitoken = dd['access']['token']['id']
print "return string is:" %dd
print "your token is : %s" %apitoken
