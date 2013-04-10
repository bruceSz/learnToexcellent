#!/usr/bin/python
#filename:getTokenUrl.py
import httplib
import json
usehttps = False

url = "9.123.106.95:5000"

osuser = "admin"
ospassword = "Passw0rd"

params = '{"auth":{"passwordCredentials":{"username":"admin","password":"Passw0rd"}}}'
headers = {"Content-Type":"application/json"}

if (usehttps == True):
    conn = httplib.HTTPSConnection(url,key_file='../../../cert/priv.perm',cert_file='../../../cert/srv_test.crt')
else:
    conn = httplib.HTTPConnection(url)
conn.request("POST","/v2.0/tokens",params,headers)

response = conn.getresponse()
data = response.read()
dd = json.loads(data)
conn.close()
print type(dd)
for key in dd.keys():
    print key,dd[key]
    print "\n\n"
#apitoken = dd['access']['token']['id']
apiurl = dd['access']['serviceCatalog']['nova'][0]['publicURL']
print "your token is :%s" %apitoken
print "your nova URL is: %s"%apiurl
