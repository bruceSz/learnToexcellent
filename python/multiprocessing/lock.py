from multiprocessing import Process,Lock
import time

def l(lock,num):
    lock.acquire()
    print 'hello num:%s'%(num)
    time.sleep(1)
    
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=l,args=(lock,num)).start()

