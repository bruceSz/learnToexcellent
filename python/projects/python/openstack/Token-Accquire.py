#!/usr/bin/python
import httplib
import json
url = "9.123.106.95:5000"
osuser = "admin"
ospassword = "Passw0rd"
params = '{"auth":{"passwordCredentials":{"username":"admin","password":"Passw0rd"},"tenantId":"03b514b1b07545879f8d3a79805a2b94"}}'
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