def smart_sort(L):
    """ worst case is n^2 """
    index1=1
    index3=len(L)-1 
    print index1,index3
    while L[index1]== 1:
        index1 += 1
    while L[index3] ==3:
        index3 -= 1

    while index1<index3:
        print L
        if L[index1]==3:
            L[index1],L[index3] = L[index3],L[index1]
            index3 -= 1
        else:
            index2 = index1+1
            print index2
            while L[index2] != 1 and index2 <= index3:
                index2 += 1

            if index2 <= index3:
                L[index1],L[index2] = L[index2],L[index1]
            else:
                index1+=1
                

        while L[index1] == 1:
            index1 += 1

    return L

def mov_back(L,start,pos,val):
    """ mov_back pos until L[pos] doesn't equal to val"""
   
    #assertEqual(L[pos],val)
    print 'the list is:',L
    print 'the start pos:',start
    print 'current pos',pos
    print 'target val:',val

    while  pos >= start and L[pos] == val:
        #print pos
        pos -= 1

    return pos
        
def test_mov_back():
    l=[6,6,6,6]
    pos=len(l)-1
    pos = mov_back(l,0,pos,val=6)
    print pos
    print l[pos]

def smart_sort_2(L):
    index1=1
    index3=len(L)-1
    

    while L[index3]==3 and index3>index1:
        index3 -= 1
    
    
    while index1<index3 and L[index1]==1 :
        index1 +=1

    if index3 <= index1:
        return L
    
    index2=index1

    while index2<index3:
        if L[index2]==3:
            L[index2],L[index3]=L[index3],L[index2]
            while index3>index2 and L[index3]==3:
                index3 -=1

        elif L[index2] ==1:
            L[index2],L[index1] = L[index1],L[index2]
            while index1<index2 and L[index1] == 1:
                index1 +=1

        else:
            index2 += 1

    return L



        
def smart_sort_3():
    """ quick sort: first use 1 as pivot and 
        exchange all 2 and 3 to right side 
        of 1.Then use 2 as pivot ,exchange 
        all 3 after all 2."""
    pass

def smart_sort_4():
    """ use 2,3,5 to replace 1,2,3 accordingly
        multiply whole input array get a val.Devide 2,3,5
        ,the times val can devide 2 with no rem represent 
        how many 1 in the array ,so forth and output result
        .It is a variation of counting sort."""

    pass


            
            
    

def test_smart_sort():
    a=[1,2,3,2,1,2,3,2,1,2,2,2,3,3,2,1,1,1,3]
    sorted_a = smart_sort_2(a)
    print sorted_a


if __name__ == '__main__':
    test_smart_sort()
    #test_mov_back()
