class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
        
    def __str__(self):
        return self.state

class YourBorg(Borg):
    pass

if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'idle'
    rm2.state = "running"
    print ('rm1:',rm1)
    print ('rm2:',rm2)
    rm2.state = 'zombie'
    print ('rm1:',rm1)
    print ('rm2:',rm2)

    print ('rm1 id:',id(rm1))
    print ('rm2 id:',id(rm2))

    rm3 = YourBorg()
    print ('rm1:',rm1)
    print ('rm2:',rm2)
    print ('rm3:',rm3)
    print ('dict of rm1:',rm1.__dict__)
    print ('dict of rm2:',rm2.__dict__)
    print ('dict of rm3:',rm3.__dict__)
