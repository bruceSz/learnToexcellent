#!/usr/bin/python
import random
DEBUG = 1
LEVEL = 0
def quick_sort(L):
    """ input L is the list about to be sorted """
    ret = []
    global LEVEL
    LEVEL = LEVEL + 1
    length = len(L)
    assert length>=0
    if length == 0 or length == 1:
	LEVEL = LEVEL - 1
	return L
    rand = random.randint(0,length-1)
    pivot = L[rand]
    
    if DEBUG == 1:
	print 'pick :',pivot

    left,right = [],[]
    for item in L[0:rand]+L[rand+1:]:
	if item>=pivot:
	    right.append(item)
	else:
	    left.append(item)
    
    if DEBUG == 1:
	print 'LEVEL:',LEVEL,'left:',left,'right:',right

    left = quick_sort(left)
    right = quick_sort(right)

    if DEBUG == 1:
	print 'LEVEL:',LEVEL,'left:',left,'right:',right

    ret = ret + left
    ret.append(pivot)
    ret = ret + right
    
    LEVEL = LEVEL - 1 
    return ret

if __name__ == '__main__':
    l=[23,54,12,19,31,0]
    print l
    l = quick_sort(l)
    print l



