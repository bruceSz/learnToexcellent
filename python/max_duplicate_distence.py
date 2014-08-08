
def find_max_dup_distance(seq):
    d = {}
    for index,value in enumerate(seq):
        if not value in d:
            d[value]=[index,0]
        else:
            ori = d[value]
            d[value] = [ori[0],index-ori[0]]

    max_v = -1
    max_distance = 0
    for k,v in d.items():
        if v[1]>max_distance:
            max_distance = v[1] 
            max_v=k
    return max_v,max_distance
            
if __name__ == '__main__':
    seq = [1,3,5,1,2,9,2,4,2,1,3,4,5,2,2,34,5]
    print find_max_dup_distance(seq)


