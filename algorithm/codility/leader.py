def goldenLeader(A):
    n = len(A)
    size = 0

def fastLeader(A):
    n = len(A)
    leader = -1
    A.sort()
    candidate = A[n//2]
    count = 0
    for i in xrange(n):
        if A[i] == candidate:
            count += 1

    if count > n//2:
        leader = count
    return count

def slowLeader(A):
    n = len(A)
    leader  = -1
    for i in xrange(n):
        candidate = A[i]
        count = 0
        for k in xrange(n):
            if A[k]==candidate:
                count += 1
        if  count > n//2:
            leader = candidate
            break

    return leader

def testLeader():
    A= [1,2,3,4,2,2,2,2,2,5]
    print fastLeader(A)

if __name__ == '__main__':
    testLeader()

