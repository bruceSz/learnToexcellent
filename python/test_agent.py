class A(object):
    def __init__(self,o):
        self.__obj__ = o

    def __getattr__(self,name):
        if hasattr(self.__obj__,name):
            return getattr(self.__obj__,name)
        return self.__dict__[name]

    def __iter__(self):
        return self.__obj__.__iter__()
    
if __name__ == '__main__':
    l = []
    a = A(l)
    for i in xrange(101):a.append(i)
    print sum(a)
