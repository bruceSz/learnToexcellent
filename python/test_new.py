import threading

DEBUG = False

class Singleton(object):
    objs = {}
    objs_locker = threading.Lock()

    def __new__(cls,*args,**kv):
        if DEBUG:
            print cls

        if cls in cls.objs:
            return cls.objs[cls]

        cls.objs_locker.acquire()
         
        try:
            if cls in cls.objs: # double lock check.Famous
                return cls.objs[cls]

            cls.objs[cls] = object.__new__(cls)
            if DEBUG:
                print cls.objs[cls]
        finally:
            cls.objs_locker.release()

        return cls.objs[cls]
                

class SingleName(Singleton):
    
    def __init__(self,name='default'):
        self.name = name
        if DEBUG:
            print self.name
        print 'init a single name instance =====',self.name


if __name__== '__main__':
    sn2 = SingleName('bruce')
    sn2 = SingleName('zs')
