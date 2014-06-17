def counting_sort(A,k):
    n = len(A)
    count = [0] * (k+1)
    for i in xrange(n):
        count[A[i]]+=1

    p = 0
    for i in xrange(k+1):
        # if count[i]==0
        # below loop will never be executed.
        # neither index p
        for j in xrange(count[i]):
            A[p]=i
            p+=1

    return A
