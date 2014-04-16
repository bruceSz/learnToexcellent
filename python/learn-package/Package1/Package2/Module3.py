print 'this is module 3'

def nth_fibo(n):
    fa = 0
    fb = 1
    if n == 1:
        return fa
    elif n == 2:
        return fb
    else:

        for i in xrange(3,n+1):
            ret = fa + fb
            fa = fb
            fb = ret

    return ret

if __name__ == '__main__':
    print nth_fibo(9)
    
