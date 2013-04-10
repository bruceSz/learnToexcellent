#!/usr/bin/python
#filename:mySimpleHttpServer.py
import SocketServer
import SimpleHTTPServer

HOST = ''
PORT = 8000
server = SocketServer.TCPServer((HOST,PORT),SimpleHTTPServer.SimpleHTTPRequestHandler)
server.serve_forever()
