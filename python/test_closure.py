def aoo(a,b):
    c = a
    def boo(x):
        x=b+1
        return x
    return boo

if __name__ == '__main__':
    test = aoo(1,9)
    print test,test(1)

    test = aoo(1,10)
    print test,test(1)

    test = aoo(1,11)
    print test(2)

