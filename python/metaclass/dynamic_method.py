def ma(cls,x):
    print 'method a : ',x

def mb(cls):
    print 'method b'


method_dict = {
        'ma' : ma,
        'mb' : mb,
}

class DynamicMethod(type):
    def __new__(cls,name,bases,dct):
        return type.__new__(cls,name,bases,dct)

    def __init__(cls,name,bases,dct):

        if name[:3]=='Abc':
            setattr(cls,'ma',ma)
            print cls.__dict__

        super(DynamicMethod,cls).__init__(name,bases,dct)

class Abctest(object):
    __metaclass__ = DynamicMethod

    def mc(self,x):
        print x*3


class NotAbc(object):
    __metaclass__ = DynamicMethod
    
    def mc(self,x):
        print x*3

def main():
    a= Abctest()
    a.mc(3)
    a.ma(5)
    print dir(a)
if __name__ == '__main__':
    main()
