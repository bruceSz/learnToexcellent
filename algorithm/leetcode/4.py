def max_sum_sub_list(l):
    maxsum = 0
    cur = 0
    for i in l:
        cur += i
        if cur > maxsum:
            maxsum = cur
        if cur <0:
            cur =0

    return maxsum

if __name__ == "__main__":
    #l= [-2,11,-4,13,-5,-2]
    l=[-6,2,4,-7,5,3,2,-1,6,-9,10,-2]
    print max_sum_sub_list(l)



        
