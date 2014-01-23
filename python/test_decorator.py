import threading
def sync(func):
    def wrapper(*args,**kv):
        self = args[0]
        self.lock.acquire()

        try:
            return func(*args,**kv)
        finally:
            self.lock.release()
    return wrapper

def Foo(object):
    def __init__(self):
        self.loc = threading.Lock()

    @sync
    def interface1(self):
        pass

    @sync
    def interface2(self):
        pass


class DecorateClass(object):
    def decorate(self):
        for name,fn in self.iter():
            if not self.filter(name,fn):
                continue
            self.operate(name,fn)


class LockerDecorator(DecorateClass):
    def __init__(self,obj,lock=threading.RLock()):
        self.obj = obj
        self.lock = lock
    def iter(self):
        return [(name,getattr(self.obj,name)) for name in dir(self.obj)]

    def filter(self,name,fn):
        if not name.startswith('_') and callable(fn):
            return True
        else:
            return False

    def operate(self,name,fn):
        def locker(*args,**kv):
            self.lock.acquire()
            try:
                return fn(*args,**kv)
            finally:
                self.lock.release()
        setattr(self.obj,name,locker)

class Foo(object):
    def __init__(self):
        LockerDecorator(self).decorate()

    def interface1(self):
        pass

    def interface2(self):
        pass

