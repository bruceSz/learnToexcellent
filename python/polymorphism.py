class base(object):
    """base class """
    def __init__(self,name):
        self.name = name
    def printest(self):
        print "base class:",self.name

class subclass1(base):
    """sub class 1"""
    def printest(self):
        print "sub class 1",self.name

class subclass2(base):
    """sub class 2"""
    def printest(self):
        print "sub class 2",self.name

class subclass3(base):
    """sub class 3 """
    pass
def testFunc(o):
    o.printest()

if __name__ == "__main__"：
    testFunc(subclass1("1"))
    testFunc(subclass2("2"))
    test
    
