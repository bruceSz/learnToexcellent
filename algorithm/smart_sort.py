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



    

def test_smart_sort():
    a=[1,2,3,2,1,2,3,2,1,2,2,2,3,3,2,1,1,1,3]
    sorted_a = smart_sort(a)
    print sorted_a


if __name__ == '__main__':
    test_smart_sort()
