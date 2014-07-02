class Solution:
    def candy(self,ratings):
        length = len(ratings)

        if length == 1:
            return 1
        if length == 0:
            return 0

        candies = [0]*length

        if  ratings[1] >= ratings[0]:
            candies[0]=1
        if ratings[length-2] >= ratings[length-1]:
            candies[length-1] = 1

        for i in xrange(1,length-1):
            if ratings[i-1] >= ratings[i] and ratings[i] <= ratings[i+1]:
                candies[i] = 1

        for i in xrange(1,length):
            if ratings[i]> ratings[i-1]:
                candies[i] = candies[i-1]+1
            
            
        for i in xrange(length-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                if (candies[i+1]+1)> candies[i]:
                    candies[i]=candies[i+1]+1

        ret = 0
        print candies
        for i in xrange(0,length):
            ret += candies[i]

        return ret
        

if __name__ == '__main__':
    ratings = [1,0,2]
    ss = Solution()
    print ss.candy(ratings)
