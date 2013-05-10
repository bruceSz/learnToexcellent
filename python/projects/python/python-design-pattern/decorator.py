class foo(object):
    def f1(self):
        print ('original f1')
    def f2(self):
        print('original f2')
    
class foo_decorator(object):
    def __init__(self,decorator):
        self._decorator = decorator
    #def f1(self):
     #   print ('decorated f1')
        self._decorator.f1()
    def __getattr__(self,name):
        return getattr(self._decorator,name)

u = foo()
v = foo_decorator(u)
v.f1()
v.f2()
