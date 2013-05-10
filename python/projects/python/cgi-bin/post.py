#!/usr/bin/env python
#filename:post.py
import cgi 
form = cgi.FieldStorage()
print "Content-Type: text/html"
print 
print "<p>hello world!</p>
print "<p>"+repr(form['firstname'])+"</p>"
