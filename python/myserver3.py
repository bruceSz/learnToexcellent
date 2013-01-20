#!/usr/bin/python
#filename:myserver3.py
import socket
HOST = ''
PORT =8000

text_content='''
HTTP/1.x 200 OK
Content-Type: text/html

<head><title>wow</title>
</head>
<html>
<p>wow,python server,from zhang song </p>
<IMG src="test.gif">
</html>
'''
f=open('test.gif','rb')
pic_content='''
HTTP/1.x 200 OK
Content-Type: image/jpg

'''
pic_content=pic_content+f.read()
f.close()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))

while True:
    s.listen(3)
    conn,addr=s.accept()
    request = conn.recv(1024)
    method = request.split(' ')[0]
    src = request.split(' ')[1]
    
    if method == 'GET':
        if src == '/test.gif':
            content=pic_content
        else : content=text_content
        print 'Connected by', addr
        print 'Request is : ',request
        conn.sendall(content)
    if method == 'POST':
        form = request.split('\r\n')
        idx = form.index('')
        entry = form[idx:]
        value = entry[-1].split('=')[-1]
        conn.sendall(text_content+'\n <p>'+value+'</p>')
    conn.close()

