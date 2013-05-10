import weakref

class Card(object):
    _CardPool = weakref.WeakValueDictionary()

    """ flywight implementation.if the object exits in the pool
    just return it"""
    def __new__(cls,value,suit):
        obj = Card._CardPool.get(value+suit,None)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value+suit] = obj
            obj.value,obj.suit = value,suit
        return obj
    def __repr__(self):
        return "<Card:%s%s>" %(self.value,self.suit)

if __name__ == '__main__':
    c1 = Card('9','h')
    c2 = Card('9','h')
    c3 = Card('9','j')
    print(c1,c2,c3)
    print(c1 == c2)
    print (id(c1),id(c2),id(c3))
    s1 = str(1)
    s2 = str(2)
    print(s1,s2)
    print(s1 == s2)
    print (id(s1),id(s2))
