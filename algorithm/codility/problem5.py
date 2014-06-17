def leastLength(A):
    # use the list simulate a queue
    ret = 0
    l=[]
    for i in A:
        if i==0:
            l.append(1)
        else:
            if len(l)>0:
                l.pop(0)
            else:
                ret+=1

    return ret


if __name__ == '__main__':
    A = [0,0,1,1,1,0,0]
    print leastLength(A)

    
