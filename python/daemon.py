def createDaemon():
    import os
    try:
        if os.fork()>0:
            os._exit(0)
    except OSError,error:
        print 'fork #1 failed:%d(%s)'%(error,errno,error.strerror)
        os._exit(0)

    os.chdir('/')
    os.setsid()
    os.umask(0)

    try:
        pid = os.fork()
        if pid > 0:
            print 'Daemon PID %d'%pid
            os._exit(0)

    except OSError,error:
        print 'fork #2 failed:%d(%s)'%(error.errno,error.strerror)
        os._exit(0)

    funcDemo()

def funcDemo():
    import time
    fd = open('/tmp/daemon.log','w')
    while True:
        fd.write(time.ctime()+'\n')
        fd.flush()
        time.sleep(2)
    fd.close()

if __name__ == '__main__':
    createDaemon()





