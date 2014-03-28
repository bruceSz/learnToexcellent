import threading

DEBUG = False

class Singleton(object):
    objs = {}
    objs_locker = threading.Lock()

    def __new__(cls,*args,**kv):
        if DEBUG:
            print cls

        if cls in cls.objs:
            return cls.objs[cls]['obj']

        cls.objs_locker.acquire()
         
        try:
            if cls in cls.objs: # double lock check.Famous
                return cls.objs[cls]['obj']

            obj = object.__new__(cls)
            cls.objs[cls]={'obj':obj,'init':False}

            setattr(cls,'__init__',cls.decorate_init(cls.__init__))

            if DEBUG:
                print cls.objs[cls]
        finally:
            cls.objs_locker.release()

        return cls.objs[cls]['obj']

    @classmethod
    def decorate_init(cls,fn):
        def init_wrap(*args):
            if DEBUG:
                print 'under wrapped init:======',cls.objs[cls]

            if not cls.objs[cls]['init']:
                fn(*args)
                cls.objs[cls]['init']=True
            return
        return init_wrap

class SingleName(Singleton):
    
    def __init__(self,name='default'):
        self.name = name
        if DEBUG:
            print self.name
        print 'init a single name instance =====',self.name


if __name__== '__main__':
    sn1 = SingleName('bruce')
    print sn1.name
    SingleName('zs')
    SingleName('simona')
    print sn1.name
