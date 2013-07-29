#!usr/bin/env python

print 'Content-Type:text/html\n'
from os.path import join,abspath

import cgi,sys

BASE_DIR = abspath('data')
form = cgi.FieldStorage()
filename = form.getvalue('filename')
if not filename:
   print 'please enter a file name'
   sys.exit()

try:
	text = open(join(BASE_DIR,filename)).read()
except Exception,data:
       print str(data)


