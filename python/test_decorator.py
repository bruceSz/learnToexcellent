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

def single(cls):
    ins = {}
    def getins(*args):
        if cls not in ins:
            ins[cls] = cls(*args)
        return ins[cls]
    return getins

@single
class A:
    def __init__(self,name):
        self.name = name
@single
class B:
    def __init__(self,count):
        self.count = count

if __name__ == '__main__':
    a1 = A('this is test1')
    print a1.name
    a2 = A("test1 is this(this is reverse ,notice!)")
    print a2.name

    print a1
    print a2

    b1 = B(1)
    print b1.count

    b2 = B(2)
    print b2.count
     
    print b1
    print b2

