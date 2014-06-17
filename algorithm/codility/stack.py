N = 10
stack = [0]*N
size = 0

def push(x):
    global size
    stack[size] = x
    size += 1

def pop():
    global size
    size -= 1
    return stack[size]


# object version 

class Stack(object):
    def __init__(self, size):
        self._stack = [0]*size
        self._size = size

    def push(self,x):
        self._stack[self._size]=x
        self._size+=1

    def pop(self):
        self._size -= 1
        return self._stack[size]

# thread safe version

import threading
class Stack2(object):
    def __init__(self,size):
        self._stack = [0]*size
        self._size = size
        self._mutex = threading.Lock() 

    def push(self,x):
        self._mutex.acquire()

        self._stack[self._size] = x
        self._size +=1

        self._mutex.release()

    def pop():
        self._mutex.acquire()
        self._size -=1
        tmp = self._stack[size]
        self._mutex.release()
        return tmp

# thread safe version
def threadsafe(func):
    def func_(self,*args,**v):
        self._mutex.acquire()
        try:
            func(self,*args,**v)
        finally:
            self._mutex.release()

    return func_

class Stack3(object):
    def __init__(self,size):
        self._stack = [0] * size
        self._size = size
        self._mutex = threading.Lock()

    @threadsafe
    def push(self,x):
        self._stack[self._size]=x
        self._size+=1

    @threadsafe
    def pop(self):
        self._size -=1
        return self._stack[self._size]
        
