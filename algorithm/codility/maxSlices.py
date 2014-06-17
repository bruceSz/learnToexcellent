def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        tmp  = max_ending + a
        if tmp >0:
            max_ending = tmp
        else:
            max_ending = 0
        if max_ending > max_slice:
            max_slice = max_ending

    return max_slice

def quadratic_max_slice(A):
    n = len(A)
    pref = [0]*(n+1)
    for i in xrange(n):
        pref[i+1] = A[i]+pref[i] 
    pref.pop(0)

    result = 0
    for p in xrange(n):
        for q in xrange(p+1,n):
            tmp = pref[q]-pref[p]
            if tmp > result:
                result = tmp

    return result


def quadratic_max_slice2(A):
    n = len(A)
    result = 0 
    for p in xrange(n):
        pref = 0
        for q in xrange(p,n):
            pref += A[q]
            if pref > result :
                result = pref

    return result


                
        
        
        
def slow_max_slice(A):
    n = len(A)
    result  = 0
    for p in xrange(n):
        for q in xrange(p+1,n):
            tmp = 0
            for i in xrange(p,q):
                tmp += A[i]
            if tmp > result :
                result = tmp

    return result

def test_quadratic_max_slice():
    A = [1,2,3,4]
    quadratic_max_slice(A)
def test_max_slice():
    A=[5,-7,3,5,-2,4,-1]
    print slow_max_slice(A)
    print quadratic_max_slice(A)
    print quadratic_max_slice2(A)
    print golden_max_slice(A)
    
if __name__ == '__main__':
    test_max_slice()
    #test_quadratic_max_slice()
