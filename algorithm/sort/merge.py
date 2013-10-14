#!/usr/bin/python
level = 0
DEBUG = 0
def merge_sort(l):
    """ the list about to be sorted , divide and sort first
	then merge them together
    """
    if DEBUG == 1: 
	global  level 
	level = level + 1

    ret = []
    length = len(l)

    if length == 1 or length == 0 :
	if DEBUG == 1: 
	   level = level - 1
	return l

    half = length/2

    left = merge_sort(l[0:half])
    if DEBUG == 1: 
	print 'left:',level,'::',left
    right = merge_sort(l[half:])
    if DEBUG == 1: 
	print 'right:',level,'::',right

    left_n = len(left)
    right_n = len(right)
    i,j = 0,0

    while i < left_n and j < right_n:
	if left[i] < right[j]:
	    ret.append(left[i])
	    i = i + 1
	else:
	    ret.append(right[j])
	    j = j + 1
    if i < left_n:
	ret = ret + left[i:]
    elif j < right_n:
	ret = ret + right[j:]
    else:
	pass
    if DEBUG == 1: 
	print 'after merge:',level,'::',ret
	level = level - 1
    return ret

if __name__ == '__main__':
    l = [4,7,2,6,1,4,7,3,5,2,6]
    print l
    l = merge_sort(l)
    print l
