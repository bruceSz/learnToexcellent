import sys
import time
import zmq

def main():
    if len(sys.argv)<2:
        print 'usage:subscriber <connect_to> [topic topic ...]'
        sys.exit(1)

    connect_to = sys.argv[1]
    topics = sys.argv[2:]
    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(connect_to)

    if not topics:
        print "Received  messages on ALL topics"
        s.setsockopt(zmq.SUBSCRIBE,"")
    else:
        print "receiving messages on topics :%s..."%topics
        for t in topics:
            s.setsockopt(zmq.SUBSCRIBE,t)

    try:
        while True:
            topic,msg = s.recv_pyobj()
            print '  Topic:%s,msg:%s'%(topic,msg)
    except KeyboardInterrupt:
        pass
    print "Done"

if __name__ == '__main__':
    main()
