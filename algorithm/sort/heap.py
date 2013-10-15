#!/usr/bin/python
DEBUG = 0
def heap_init(L):
    """ L is the list about to be adjusted to a heap """
    length = len(L)
    assert L>=0
    if length == 1:
	return L

    for i in range((length-2)/2,-1,-1):
	if DEBUG == 1:
	    print i
	while i<=length-1:
	    
	    j = 2*i+1 
	    if j>length-1:
		break
	    if j+1 <= length-1:
		if L[j]>L[j+1]:
		    j=j+1
	    if L[j]<L[i]:
		L[i],L[j]=L[j],L[i]
	    i = j
	    if DEBUG == 1:
		print L
    return L
    

def heap_sort(L):
    """L is the list about to be sorted"""
    L = heap_init(L)
    
if __name__ == '__main__':
    l=[23,54,12,19,31,0]
    print l
    l = heap_init(l)
    print l
