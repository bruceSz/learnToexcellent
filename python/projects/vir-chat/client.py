import socket
import time

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientsocket.connect(('',8888))
while True:
    time.sleep(2)
    clientsocket.send('hello zs')
    print clientsocket.recv(1024)

clientsocket.close()
