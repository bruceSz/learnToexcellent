def findSmallestPalinNumber(l):
    assert(isinstance(l,list)==True)
    ret = copy.copy(l)
    length = len(ret)
    pre = int(ret[length/2-1])
    nex = int(ret[length/2])
    if length%2==0 and pre != nex:
        if pre<nex:
            ret[length/2-1]=pre+1
        for i in range(length/2):
            ret[length-1-i] = ret[i]


    else:
        if (length%2!=0 and nex != 9) or (length%2==0 and pre == nex and nex != 9):
            carry = False
            for i in range(length/2):
                if ret[length-1-i] > ret[i]:
                    
                    curry = True

                elif ret[length-1-i]== ret[i]:
                    pass
                else:
                    if curry == True:
                        curry = False

                ret[length-1-i]=ret[i]

            if curry = True:
                if length%2 == 0:

                    #pre == nex
                    ret[length/2-1] = str(pre+1)
                    ret[length/2] = str(nex+1)
                else:
                    ret[length/2] = str(nex+1)

        else:
            
            carry = False
            for i in range(length/2):
                if ret[length-1-i] > ret[i]:
                    curry = True
                elif ret[length-1-i]== ret[i]:
                    pass
                else:
                    if curry == True:
                        curry = False
                ret[length-1-i]=ret[i]

            if curry == True:
                j = length/2
                while ret[j]==str(9):
                    j--
                if j<0:
                    ret = [str(0) for i in ret]
                    ret.insert(0,str(1))
                    ret[len(length)]=str(1)

                else:
                    ret[length/2]=str(0)
                    # for length%2==0 situation, at the loop will run atleast once.
                    for pos in range(j+1,length/2):
                        ret[pos]=str(0)
                        ret[length-1-pos]=str(0)

                    for i in range(j):
                        ret[length-1-i]=ret[i]

    return ret

                        
                    
