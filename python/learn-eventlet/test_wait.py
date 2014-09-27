from eventlet import greenpool
from eventlet import event
import time

SLEEP_TIME = 3
POOL_SIZE = 5
done = event.Event()

def sleep_and_echo(msg):
    while True:
        print msg
        time.sleep(SLEEP_TIME)

def sleep_send_event(msg):
    count = 0
    while True:
        print msg
        count += 1
        if count >= 3:
            if done.ready():
                
        time.sleep(SLEEP_TIME)



if __name__ == '__main__':
    pool = greenpool.GreenPool(POOL_SIZE)
    gt = pool.spawn(sleep_send_event,'test hello!')
    gt.wait()
    print 'main greenthread end'
