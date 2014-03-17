#!/usr/bin/python
#encoding:utf8

import cgi
import cgitb
import sys
import os
environ = {}
environ['REQUEST_METHOD'] = os.environ['REQUEST_METHOD']
environ['SCRIPT_NAME'] = os.environ['SCRIPT_NAME']
environ['PATH_INFO'] = os.environ['PATH_INFO']
environ['QUERY_STRING'] = os.environ['QUERY_STRING']

