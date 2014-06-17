def goldenLeader(A):
    n = len(A)
    # size is the depth of stack
    size = 0
    for i in xrange(n):
        if size == 0:
            candidate = A[i]
            size += 1
        else:
            if A[i]==candidate:
                size += 1
            else:
                size -= 1

    return candidate
                
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
    print goldenLeader(A)

if __name__ == '__main__':
    testLeader()

