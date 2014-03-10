class C(object):
    a = 'abc'
    def __getattribute__(self,*args,**kwargs):
        print "__getattribute__ is called"
        return object.__getattribute__(self,*args,**kwargs)

    def __getattr__(self,name):
        print ('__getattr() is called')
        return name+"from getattr"

    def __get__(self,instance,owner):
        print '__get__ is called'
        return self

    def foo(self,x):
        print(x)

class C2(object):
    d = C()

if __name__ == "__main__":
    c = C()
#    c.foo(3)
#    c2 = C2()
#    c.a
#    print(c.a)
    print(c.zzz)
#    c2.d
#    print(c2.d.a)


