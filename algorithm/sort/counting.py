#!/usr/bin/python
# DEBUG level can be set to 0,1,2 which indicate the detail level of the debug info ,the bigger the number is,the more detail output will become.
DEBUG = 1
MAX_NUMBER = 100
def counting_sort(L):
    d = {}
    Ret = []
    for i in range(0,len(L)):
	Ret.append(0)
    if DEBUG == 2:
	print Ret

    for i in range(0,MAX_NUMBER+1):
	d[i] = 0

    for i in range(0,len(L)):
	d[L[i]] = d[L[i]] + 1

	    
    if DEBUG == 1:
	for k,v in d.items():
	    if d[k] != 0:
		print k,v
	print 

    for i in range(1,MAX_NUMBER+1):
	d[i] = d[i]+d[i-1]

    if DEBUG == 2:
	for k,v in d.items():
	    if d[k] != 0:
		print k,v
    for i in range(len(L)-1,-1,-1):
        # as the algorithm goes,d[i] will be 0 when same corresponding  value in L are all traversed.
	if DEBUG == 1:
	    print L[i],d[L[i]]
	Ret[d[L[i]]-1] = L[i] 
	d[i] = d[i] - 1

    return Ret
	
	
if __name__ == '__main__':
    L = [34,21,59,67,46,93,55]
    print L
    L = counting_sort(L)
    print L

