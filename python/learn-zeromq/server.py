import zmq
c = zmq.Context()
s=c.socket(zmq.REP)
s.bind('tcp://127.0.0.1:10001')
while True:
    msg = s.recv_pyobj()
    s.send_pyobj(msg)
s.close()
