import A as this
class A:
    def a(self):
        pass

    
class A1(A):
    def a1(self):
        pass

curMod = dir()

class B:
    def b(self):
        pass

if __name__ == '__main__':
    print('dir current file in half',curMod)
    print('dir current file',dir())
    print('dir current file import as: ',dir(this))
    print('dir current file from sys modules',dir(sys.modules[__name__]))
