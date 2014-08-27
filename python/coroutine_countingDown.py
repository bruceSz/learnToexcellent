def countdown(n):
    print "counting down from,",n
    while n>=0:
        newv = (yield n)
        if newv is not None:
            n = newv

        else:
            n -= 1

if __name__ == '__main__':
    c = countdown(5)
    for i in c:
        print i
        if i==5:
            print c.send(3)

