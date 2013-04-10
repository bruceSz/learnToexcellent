#!/usr/bin/python
#filename:myCGIHTTPServer.py
import BaseHTTPServer
import CGIHTTPServer
HOST = ''
PORT = 8000
server = BaseHTTPServer.HTTPServer((HOST,PORT),CGIHTTPServer.CGIHTTPRequestHandler)

server.serve_forever()
