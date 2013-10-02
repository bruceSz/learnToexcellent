#!/usr/bin/python
def permute(p,l,length):
    """ p is for print
	if length is 0 print the p tuple 
	otherwise iterate.
    """
    assert length >= 0
    if length == 0:
	print p
	return

    for i in range(0,length):
	n = p + (l[i],) 
	permute(n,l[0:i]+l[i+1:],length-1)
    

if __name__ == '__main__':
    l = [1,2,3,4]
    permute((),l,4)

