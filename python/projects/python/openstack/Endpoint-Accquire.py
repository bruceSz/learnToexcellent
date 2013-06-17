#!/usr/bin/python
import httplib
import json

#usehttps = True
url = "9.123.137.200:5000"
osuser="admin"
ospassword="Passw0rd"

params = '{"auth":{"passwordCredentials":{"username":"admin","password":"Passw0rd"},"tenantId":"fd881b9cdc904e33871d5038f6397c4c"}}'
headers = {"Content-Type":"application/json"}

conn = httplib.HTTPConnection(url)
conn.request("POST","/v2.0/tokens",params,headers)
# http response
response = conn.getresponse()
data = response.read()
dd = json.loads(data)
conn.close()
#print data
apitoken = dd['access']['token']['id']
apiCatalogs = dd['access']['serviceCatalog'] 
for catalog in apiCatalogs:
    #print catalog
    #print '\n'
    print "%s 's endpoint is :%s" %(catalog['name'],catalog['endpoints'][0]['publicURL'])
#apiurl = dd['access']['serviceCatalog'][2]['endpoints'][0]['publicURL']
#apiname = dd['access']['serviceCatalog'][2]['name']
#print "you nova urlis :"%apiurl
