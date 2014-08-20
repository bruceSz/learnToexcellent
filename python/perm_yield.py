def y_perm(items):
    if len(items)==1:
        yield items
    else:
        for i,_ in enumerate(items):
            v = items[i:i+1]
            rest = items[:i]+items[i+1:]
            
            for p in y_perm(rest):
                
                yield v+p



def perm(items):
    ret = []
    if len(items)==1:
        ret.append(items)
        return ret
    for i,_ in enumerate(items):
        v = items[i:i+1]
        rest = items[:i]+items[i+1:]
        #for i in tmp:
        #    i.append(v)
        #map(lambda x:x+v,tmp)
       
        ret.extend(map(lambda x:x+v,perm(rest)))

    return ret

if __name__ == '__main__':
    print perm('abc')
    for p in y_perm('def'):
        print p
        #pass
    
