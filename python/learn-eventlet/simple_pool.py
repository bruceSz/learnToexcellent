import eventlet
from eventlet import event
import time
evt = event.Event()

def sleep_time(sec):
    print 'begin to sleep for %s seL' %sec
    time.sleep(sec)
    #evt.send(sec)
    print 'end of sleep,wake up'
    #eventlet.sleep(0)
    print 'end of sleep sleep!!!'
    evt.wait()


def event_waiter():
    print 'wait for event',time.time()
    #evt.wait()
    print 'event has come',time.time()

if __name__ == '__main__':
    pool = eventlet.GreenPool(5)
    gt2 = eventlet.spawn(event_waiter)
    gt = eventlet.spawn(sleep_time,3)
    gt.wait()
    print 'after wait'
