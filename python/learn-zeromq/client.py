import zmq
c=zmq.Context()
s = c.socket(zmq.REQ)
s.connect('tcp://127.0.0.1:10001')
s.send_pyobj('hello')
msg = s.recv_pyobj()
print msg
