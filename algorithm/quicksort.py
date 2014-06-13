def quicksort(l):
    if len(l)<=1:
        return l

    ll = []
    lr = []
    pivot = l[0]
    l.pop(0)
    for item in l:
        if item <pivot:
            ll.append(item)
        else:
            lr.append(item)

    ll = quicksort(ll)
    lr = quicksort(lr)


    ll.append(pivot)
    ll.extend(lr)
    return ll
    


def test():
    l=[3,42,5,2,9,65]
    print l
    retl = quicksort(l)
    print retl
        
if __name__ == '__main__':
    test()
