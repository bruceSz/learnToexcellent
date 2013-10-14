#!/usr/bin/python
def insert_sort(l):
    """ l is the input list"""
    length = len(l)
    for i in range(1,length):
	cur = l[i]
	j = i-1
	while j>=0 and l[j]>cur:
	    l[j+1] = l[j]
	    j=j-1
	    
	l[j+1]=cur

    return l
	
if __name__ == '__main__':
    l=[5,2,4,6,1,3]
    print 'before:',l
    l=insert_sort(l)
    print l
	

